"""
QWaylandQuickSurface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandquicksurface.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QWaylandSurface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QWaylandClient, QWaylandCompositor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWaylandClient = WAIT['QWaylandClient']
  QWaylandCompositor = WAIT['QWaylandCompositor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandQuickSurface(QWaylandSurface):
  """
  The cute side of Qt's QWaylandQuickSurface: a plain Python object standing
  in front of one C++ QWaylandQuickSurface.

  It is built on the cute 'QWaylandSurface', as Qt's QWaylandQuickSurface is
  built on Qt's QWaylandSurface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandQuickSurface that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr',
  'useTextureAlpha', 'setUseTextureAlpha', 'useTextureAlphaChanged'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandQuickSurface::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWaylandQuickSurface::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandQuickSurfacePrivate *QWaylandQuickSurface::d_func()': gives
    'QWaylandQuickSurfacePrivate', which has no cute class yet.
  - Qt's 'const QWaylandQuickSurfacePrivate *QWaylandQuickSurface::d_func()
    const': gives 'QWaylandQuickSurfacePrivate', which has no cute class yet.
  - Qt's 'QQmlListProperty<QObject> QWaylandQuickSurface::data()': gives a
    type Python has no way to take yet.
  - Qt's 'void QWaylandQuickSurface::appendFunction(QQmlListProperty<QObject>
    *list, QObject *object)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
  - Qt's 'qsizetype
    QWaylandQuickSurface::countFunction(QQmlListProperty<QObject> *list)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject *QWaylandQuickSurface::atFunction(QQmlListProperty<QObject>
    *list, qsizetype index)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
  - Qt's 'void QWaylandQuickSurface::clearFunction(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QWaylandQuickSurface::~QWaylandQuickSurface()': the destructor:
    Python never removes a C++ QWaylandQuickSurface.
  - Qt's
    'QWaylandQuickSurface::QWaylandQuickSurface(QWaylandQuickSurfacePrivate
    &dptr)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandQuickSurface is created at the first use, not by
    'QWaylandQuickSurface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandQuickSurface.
  - Qt tells when it has removed the C++ QWaylandQuickSurface. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWaylandQuickSurface that has no cute function yet,
    'appendFunction', 'atFunction', 'clearFunction', 'countFunction', 'data',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString QWaylandQuickSurface::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquicksurface.html#tr

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
    #  QString QWaylandQuickSurface::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QWaylandQuickSurface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandQuickSurface'

  #  A C++ QWaylandQuickSurface Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandQuickSurface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandQuickSurface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquicksurface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandQuickSurface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QWaylandQuickSurface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def useTextureAlpha(self) -> bool:
    """
    Calls Qt's 'bool QWaylandQuickSurface::useTextureAlpha() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquicksurface.html#useTextureAlpha
    """
    #  bool QWaylandQuickSurface::useTextureAlpha() const
    return self.uglySide.call(
        'ritual_ZNK20QWaylandQuickSurface15useTextureAlphaEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setUseTextureAlpha(self, useTextureAlpha: bool) -> None:
    """
    Calls Qt's 'void QWaylandQuickSurface::setUseTextureAlpha(bool
    useTextureAlpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquicksurface.html#setUseTextureAlpha

    Parameters
    ----------

    useTextureAlpha : bool
      Passed on as it is.
    """
    #  void QWaylandQuickSurface::setUseTextureAlpha(bool useTextureAlpha)
    self.uglySide.call(
        'ritual_ZN20QWaylandQuickSurface18setUseTextureAlphaEb',
        useTextureAlpha,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandQuickSurface::QWaylandQuickSurface()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquicksurface.html#QWaylandQuickSurface
    """
    #  QWaylandQuickSurface::QWaylandQuickSurface()
    self._noteCreation(QWaylandQuickSurface, lambda: Rituals.call(
        'ritual_ZN20QWaylandQuickSurfaceC1Ev',
    ))

  @overload(QWaylandCompositor, QWaylandClient, int, int)
  @overload(QWaylandCompositor, NoneType, int, int)
  @overload(NoneType, QWaylandClient, int, int)
  @overload(NoneType, NoneType, int, int)
  def __init__(
      self,
      compositor: Optional[QWaylandCompositor],
      client: Optional[QWaylandClient],
      id: int,
      version: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandQuickSurface::QWaylandQuickSurface(QWaylandCompositor
    *compositor, QWaylandClient *client, quint32 id, int version)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquicksurface.html#QWaylandQuickSurface

    Parameters
    ----------

    compositor : Optional[QWaylandCompositor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    client : Optional[QWaylandClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : int
      Passed on as it is.

    version : int
      Passed on as it is.
    """
    #  QWaylandQuickSurface::QWaylandQuickSurface(QWaylandCompositor
    #      *compositor, QWaylandClient *client, quint32 id, int version)
    self._noteCreation(QWaylandQuickSurface, lambda: Rituals.call(
        'ritual_ZN20QWaylandQuickSurfaceC1EP18QWaylandCompositorP14QWayland'
        'Clientji',
        self._addressOf(compositor), self._addressOf(client), id, version,
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

  def useTextureAlphaChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickSurface::useTextureAlphaChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquicksurface.html#useTextureAlphaChanged
    """
    #  void QWaylandQuickSurface::useTextureAlphaChanged()
    self.uglySide.call(
        'ritual_ZN20QWaylandQuickSurface22useTextureAlphaChangedEv',
    )

  @staticmethod
  def appendFunction(*__, **_) -> Never:
    """
    Qt's 'void QWaylandQuickSurface::appendFunction(QQmlListProperty<QObject>
    *list, QObject *object)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandQuickSurface.appendFunction' has no cute function yet. "
        "Qt's 'void "
        "QWaylandQuickSurface::appendFunction(QQmlListProperty<QObject> "
        "*list, QObject *object)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def atFunction(*__, **_) -> Never:
    """
    Qt's 'QObject *QWaylandQuickSurface::atFunction(QQmlListProperty<QObject>
    *list, qsizetype index)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandQuickSurface.atFunction' has no cute function yet. Qt's "
        "'QObject "
        "*QWaylandQuickSurface::atFunction(QQmlListProperty<QObject> *list, "
        "qsizetype index)': names 'QQmlListProperty<QObject>', which has no "
        "cute class yet.")

  @staticmethod
  def clearFunction(*__, **_) -> Never:
    """
    Qt's 'void QWaylandQuickSurface::clearFunction(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandQuickSurface.clearFunction' has no cute function yet. "
        "Qt's 'void "
        "QWaylandQuickSurface::clearFunction(QQmlListProperty<QObject> "
        "*list)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def countFunction(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QWaylandQuickSurface::countFunction(QQmlListProperty<QObject> *list)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandQuickSurface.countFunction' has no cute function yet. "
        "Qt's 'qsizetype "
        "QWaylandQuickSurface::countFunction(QQmlListProperty<QObject> "
        "*list)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QWaylandQuickSurface::data()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWaylandQuickSurface.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QWaylandQuickSurface::data()': gives a "
        "type Python has no way to take yet.")
