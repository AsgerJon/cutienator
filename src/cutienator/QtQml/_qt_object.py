"""
QtObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlbuiltinfunctions_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QtObject to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QLocale, QObject, QStringList
from . import QQmlComponent, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QDate, QDateTime, QMetaObject, QPointF
  from ..QtCore import QRectF, QSizeF, QTime, QUrl, QVariant
  from . import QJSEngine, QJSValue, QQmlApplication, QQmlEngine
  from . import QQmlPlatform, QQmlV4Function
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QDate = WAIT['QDate']
  QDateTime = WAIT['QDateTime']
  QJSEngine = WAIT['QJSEngine']
  QJSValue = WAIT['QJSValue']
  QQmlEngine = WAIT['QQmlEngine']
  QQmlV4Function = WAIT['QQmlV4Function']
  QTime = WAIT['QTime']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QtObject(QObject):
  """
  The cute side of Qt's QtObject: a plain Python object standing in front of
  one C++ QtObject.

  It is built on the cute 'QObject', as Qt's QtObject is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtObject that has a ritual and that Python can call
  so far, 52 names in all: 'metaObject', 'tr', 'qmlExtendedNamespace',
  'create', 'include', 'isQtObject', 'color', 'rgba', 'hsla', 'hsva',
  'colorEqual', 'rect', 'point', 'size', 'vector2d', 'vector3d', 'vector4d',
  'quaternion', 'matrix4x4', 'lighter', 'darker', 'alpha', 'tint',
  'formatDate', 'formatTime', 'formatDateTime', 'locale', 'url',
  'resolvedUrl', 'openUrlExternally', 'font', 'fontFamilies', 'md5', 'btoa',
  'atob', 'escapeHtml', 'quit', 'exit', 'createQmlObject', 'createComponent',
  'binding', 'callLater', 'uiLanguage', 'setUiLanguage', 'uiLanguageChanged',
  'platform', 'application', 'inputMethod', 'styleHints', 'qmlEngine',
  'jsEngine', 'v4Engine'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtObject::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QtObject::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QtObject::qt_qmlMarker_singleton()': one of Qt's own inner
    workings.
  - Qt's 'void QtObject::qt_qmlMarker_extendedNamespace()': one of Qt's own
    inner workings.
  - Qt's 'double QtObject::enumStringToValue(const QJSManagedValue &enumType,
    const QString &string)': takes a type Python has no way to hand over yet.
  - Qt's 'QString QtObject::enumValueToString(const QJSManagedValue
    &enumType, double value)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QStringList QtObject::enumValueToStrings(const QJSManagedValue
    &enumType, double value)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QBindable<QString> QtObject::uiLanguageBindable()': gives a type
    Python has no way to take yet.
  - Qt's 'Contexts QtObject::getContexts() const': gives a type Python has no
    way to take yet.

  What has no ritual
  ------------------

  3 of the 97 functions Qt declares: 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QtObject is created at the first use, not by 'QtObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtObject.
  - Qt tells when it has removed the C++ QtObject. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QtObject that has no cute function yet,
    'enumStringToValue', 'enumValueToString', 'enumValueToStrings',
    'getContexts', 'retrieveFromEnum', 'uiLanguageBindable', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QtObject, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class LoadingMode(CuteNum):
    """
    The enum 'QtObject::LoadingMode' of Qt, with the 2 names Qt gives in it.
    """

    Asynchronous = Kee[int](0)
    Synchronous = Kee[int](1)

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
    Calls Qt's 'QString QtObject::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#tr

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
    #  QString QtObject::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8QtObject2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QtObject::qmlExtendedNamespace()'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#qmlExtendedNamespace

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtObject::qmlExtendedNamespace()
    address = Rituals.call('ritual_ZN8QtObject20qmlExtendedNamespaceEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @staticmethod
  @overload(QQmlEngine, QJSEngine)
  @overload(QQmlEngine, NoneType)
  @overload(NoneType, QJSEngine)
  @overload(NoneType, NoneType)
  def create(
      a0: Optional[QQmlEngine],
      jsEngine: Optional[QJSEngine],
  ) -> Optional[QtObject]:
    """
    Calls Qt's 'QtObject *QtObject::create(QQmlEngine *a0, QJSEngine
    *jsEngine)'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#create

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    jsEngine : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QtObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtObject *QtObject::create(QQmlEngine *a0, QJSEngine *jsEngine)
    address = Rituals.call(
        'ritual_ZN8QtObject6createEP10QQmlEngineP9QJSEngine',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(jsEngine),
    )
    return QtObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QtObject::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtObject::metaObject() const
    address = self.uglySide.call('ritual_ZNK8QtObject10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(str, QJSValue)
  def include(self, url: str, callback: QJSValue) -> QJSValue:
    """
    Calls Qt's 'QJSValue QtObject::include(const QString &url, const QJSValue
    &callback) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#include

    Parameters
    ----------

    url : str
      Passed on as it is: a QString is made of it for the call.

    callback : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QtObject::include(const QString &url, const QJSValue
    #      &callback) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject7includeERK7QStringRK8QJSValue',
        url, self._valueOf(callback),
    )
    from . import QJSValue
    return QJSValue._cuteOwning(address)

  @overload(QJSValue)
  def isQtObject(self, value: QJSValue) -> bool:
    """
    Calls Qt's 'bool QtObject::isQtObject(const QJSValue &value) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#isQtObject

    Parameters
    ----------

    value : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  bool QtObject::isQtObject(const QJSValue &value) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject10isQtObjectERK8QJSValue', self._valueOf(value),
    )

  @overload(str)
  def color(self, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant QtObject::color(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#color

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtObject::color(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject5colorERK7QString', name,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(float, float, float)
  @overload(float, float, float, float)
  def rgba(self, r: float, g: float, b: float, a: float = 1.0) -> QVariant:
    """
    Calls Qt's 'QVariant QtObject::rgba(double r, double g, double b, double
    a) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#rgba

    Parameters
    ----------

    r : float
      Passed on as it is.

    g : float
      Passed on as it is.

    b : float
      Passed on as it is.

    a : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtObject::rgba(double r, double g, double b, double a) const
    address = self.uglySide.call('ritual_ZNK8QtObject4rgbaEdddd', r, g, b, a)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(float, float, float)
  @overload(float, float, float, float)
  def hsla(self, h: float, s: float, l: float, a: float = 1.0) -> QVariant:
    """
    Calls Qt's 'QVariant QtObject::hsla(double h, double s, double l, double
    a) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#hsla

    Parameters
    ----------

    h : float
      Passed on as it is.

    s : float
      Passed on as it is.

    l : float
      Passed on as it is.

    a : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtObject::hsla(double h, double s, double l, double a) const
    address = self.uglySide.call('ritual_ZNK8QtObject4hslaEdddd', h, s, l, a)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(float, float, float)
  @overload(float, float, float, float)
  def hsva(self, h: float, s: float, v: float, a: float = 1.0) -> QVariant:
    """
    Calls Qt's 'QVariant QtObject::hsva(double h, double s, double v, double
    a) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#hsva

    Parameters
    ----------

    h : float
      Passed on as it is.

    s : float
      Passed on as it is.

    v : float
      Passed on as it is.

    a : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtObject::hsva(double h, double s, double v, double a) const
    address = self.uglySide.call('ritual_ZNK8QtObject4hsvaEdddd', h, s, v, a)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant, QVariant)
  def colorEqual(self, lhs: QVariant, rhs: QVariant) -> bool:
    """
    Calls Qt's 'bool QtObject::colorEqual(const QVariant &lhs, const QVariant
    &rhs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#colorEqual

    Parameters
    ----------

    lhs : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    rhs : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QtObject::colorEqual(const QVariant &lhs, const QVariant &rhs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK8QtObject10colorEqualERK8QVariantS2_',
        self._valueOf(lhs), self._valueOf(rhs),
    )

  @overload(float, float, float, float)
  def rect(self, x: float, y: float, width: float, height: float) -> QRectF:
    """
    Calls Qt's 'QRectF QtObject::rect(double x, double y, double width,
    double height) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#rect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QtObject::rect(double x, double y, double width, double height)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject4rectEdddd', x, y, width, height,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(float, float)
  def point(self, x: float, y: float) -> QPointF:
    """
    Calls Qt's 'QPointF QtObject::point(double x, double y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#point

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QtObject::point(double x, double y) const
    address = self.uglySide.call('ritual_ZNK8QtObject5pointEdd', x, y)
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(float, float)
  def size(self, width: float, height: float) -> QSizeF:
    """
    Calls Qt's 'QSizeF QtObject::size(double width, double height) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#size

    Parameters
    ----------

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QtObject::size(double width, double height) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject4sizeEdd', width, height,
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  @overload(float, float)
  def vector2d(self, x: float, y: float) -> QVariant:
    """
    Calls Qt's 'QVariant QtObject::vector2d(double x, double y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#vector2d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtObject::vector2d(double x, double y) const
    address = self.uglySide.call('ritual_ZNK8QtObject8vector2dEdd', x, y)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(float, float, float)
  def vector3d(self, x: float, y: float, z: float) -> QVariant:
    """
    Calls Qt's 'QVariant QtObject::vector3d(double x, double y, double z)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#vector3d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtObject::vector3d(double x, double y, double z) const
    address = self.uglySide.call('ritual_ZNK8QtObject8vector3dEddd', x, y, z)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(float, float, float, float)
  def vector4d(self, x: float, y: float, z: float, w: float) -> QVariant:
    """
    Calls Qt's 'QVariant QtObject::vector4d(double x, double y, double z,
    double w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#vector4d

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    w : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtObject::vector4d(double x, double y, double z, double w)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject8vector4dEdddd', x, y, z, w,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(float, float, float, float)
  def quaternion(
      self,
      scalar: float,
      x: float,
      y: float,
      z: float,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QtObject::quaternion(double scalar, double x, double
    y, double z) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#quaternion

    Parameters
    ----------

    scalar : float
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtObject::quaternion(double scalar, double x, double y,
    #      double z) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject10quaternionEdddd', scalar, x, y, z,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload()
  def matrix4x4(self) -> QVariant:
    """
    Calls Qt's 'QVariant QtObject::matrix4x4() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#matrix4x4

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtObject::matrix4x4() const
    address = self.uglySide.call('ritual_ZNK8QtObject9matrix4x4Ev')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(
      float, float, float, float, float, float, float, float, float, float,
      float, float, float, float, float, float,
  )
  def matrix4x4(
      self,
      m11: float,
      m12: float,
      m13: float,
      m14: float,
      m21: float,
      m22: float,
      m23: float,
      m24: float,
      m31: float,
      m32: float,
      m33: float,
      m34: float,
      m41: float,
      m42: float,
      m43: float,
      m44: float,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QtObject::matrix4x4(double m11, double m12, double
    m13, double m14, double m21, double m22, double m23, double m24, double
    m31, double m32, double m33, double m34, double m41, double m42, double
    m43, double m44) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#matrix4x4

    Parameters
    ----------

    m11 : float
      Passed on as it is.

    m12 : float
      Passed on as it is.

    m13 : float
      Passed on as it is.

    m14 : float
      Passed on as it is.

    m21 : float
      Passed on as it is.

    m22 : float
      Passed on as it is.

    m23 : float
      Passed on as it is.

    m24 : float
      Passed on as it is.

    m31 : float
      Passed on as it is.

    m32 : float
      Passed on as it is.

    m33 : float
      Passed on as it is.

    m34 : float
      Passed on as it is.

    m41 : float
      Passed on as it is.

    m42 : float
      Passed on as it is.

    m43 : float
      Passed on as it is.

    m44 : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtObject::matrix4x4(double m11, double m12, double m13,
    #      double m14, double m21, double m22, double m23, double m24, double
    #      m31, double m32, double m33, double m34, double m41, double m42,
    #      double m43, double m44) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject9matrix4x4Edddddddddddddddd',
        m11, m12, m13, m14, m21, m22, m23, m24, m31, m32, m33, m34, m41, m42,
        m43, m44,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QJSValue)
  def matrix4x4(self, value: QJSValue) -> QVariant:
    """
    Calls Qt's 'QVariant QtObject::matrix4x4(const QJSValue &value) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#matrix4x4

    Parameters
    ----------

    value : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtObject::matrix4x4(const QJSValue &value) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject9matrix4x4ERK8QJSValue', self._valueOf(value),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QJSValue)
  @overload(QJSValue, float)
  def lighter(self, color: QJSValue, factor: float = 1.5) -> QVariant:
    """
    Calls Qt's 'QVariant QtObject::lighter(const QJSValue &color, double
    factor) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#lighter

    Parameters
    ----------

    color : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    factor : float
      Passed on as it is. May be left out, as in Qt: it is then 1.5.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtObject::lighter(const QJSValue &color, double factor) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject7lighterERK8QJSValued',
        self._valueOf(color), factor,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QJSValue)
  @overload(QJSValue, float)
  def darker(self, color: QJSValue, factor: float = 2.0) -> QVariant:
    """
    Calls Qt's 'QVariant QtObject::darker(const QJSValue &color, double
    factor) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#darker

    Parameters
    ----------

    color : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    factor : float
      Passed on as it is. May be left out, as in Qt: it is then 2.0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtObject::darker(const QJSValue &color, double factor) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject6darkerERK8QJSValued',
        self._valueOf(color), factor,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QJSValue, float)
  def alpha(self, baseColor: QJSValue, value: float) -> QVariant:
    """
    Calls Qt's 'QVariant QtObject::alpha(const QJSValue &baseColor, double
    value) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#alpha

    Parameters
    ----------

    baseColor : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    value : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtObject::alpha(const QJSValue &baseColor, double value)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject5alphaERK8QJSValued',
        self._valueOf(baseColor), value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QJSValue, QJSValue)
  def tint(self, baseColor: QJSValue, tintColor: QJSValue) -> QVariant:
    """
    Calls Qt's 'QVariant QtObject::tint(const QJSValue &baseColor, const
    QJSValue &tintColor) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#tint

    Parameters
    ----------

    baseColor : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    tintColor : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtObject::tint(const QJSValue &baseColor, const QJSValue
    #      &tintColor) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject4tintERK8QJSValueS2_',
        self._valueOf(baseColor), self._valueOf(tintColor),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QDate, str)
  def formatDate(self, date: QDate, format: str) -> str:
    """
    Calls Qt's 'QString QtObject::formatDate(QDate date, const QString
    &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatDate

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatDate(QDate date, const QString &format) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatDateE5QDateRK7QString',
        self._valueOf(date), format,
    )

  @overload(QDateTime, str)
  def formatDate(self, dateTime: QDateTime, format: str) -> str:
    """
    Calls Qt's 'QString QtObject::formatDate(const QDateTime &dateTime, const
    QString &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatDate

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatDate(const QDateTime &dateTime, const QString
    #      &format) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatDateERK9QDateTimeRK7QString',
        self._valueOf(dateTime), format,
    )

  @overload(str, str)
  def formatDate(self, string: str, format: str) -> str:
    """
    Calls Qt's 'QString QtObject::formatDate(const QString &string, const
    QString &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatDate

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatDate(const QString &string, const QString
    #      &format) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatDateERK7QStringS2_', string, format,
    )

  @overload(QDate, Qt.DateFormat)
  def formatDate(self, date: QDate, format: Qt.DateFormat) -> str:
    """
    Calls Qt's 'QString QtObject::formatDate(QDate date, Qt::DateFormat
    format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatDate

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.

    format : Qt.DateFormat
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatDate(QDate date, Qt::DateFormat format) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatDateE5QDateN2Qt10DateFormatE',
        self._valueOf(date), format.value,
    )

  @overload(QDateTime, Qt.DateFormat)
  def formatDate(self, dateTime: QDateTime, format: Qt.DateFormat) -> str:
    """
    Calls Qt's 'QString QtObject::formatDate(const QDateTime &dateTime,
    Qt::DateFormat format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatDate

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    format : Qt.DateFormat
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatDate(const QDateTime &dateTime, Qt::DateFormat
    #      format) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatDateERK9QDateTimeN2Qt10DateFormatE',
        self._valueOf(dateTime), format.value,
    )

  @overload(str, Qt.DateFormat)
  def formatDate(self, string: str, format: Qt.DateFormat) -> str:
    """
    Calls Qt's 'QString QtObject::formatDate(const QString &string,
    Qt::DateFormat format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatDate

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : Qt.DateFormat
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatDate(const QString &string, Qt::DateFormat
    #      format) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatDateERK7QStringN2Qt10DateFormatE',
        string, format.value,
    )

  @overload(QDate)
  @overload(QDate, QLocale)
  @overload(QDate, QLocale, QLocale.FormatType)
  def formatDate(
      self,
      date: QDate,
      locale: Optional[QLocale] = None,
      formatType: QLocale.FormatType = QLocale.FormatType.ShortFormat,
  ) -> str:
    """
    Calls Qt's 'QString QtObject::formatDate(QDate date, const QLocale
    &locale, QLocale::FormatType formatType) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatDate

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.

    locale : Optional[QLocale]
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own. May be left out, as in Qt: a new 'QLocale()' is then passed on.

    formatType : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.ShortFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatDate(QDate date, const QLocale &locale,
    #      QLocale::FormatType formatType) const
    if locale is None:
      locale = QLocale()
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatDateE5QDateRK7QLocaleNS1_10FormatTypeE',
        self._valueOf(date), self._valueOf(locale), formatType.value,
    )

  @overload(QDateTime)
  @overload(QDateTime, QLocale)
  @overload(QDateTime, QLocale, QLocale.FormatType)
  def formatDate(
      self,
      dateTime: QDateTime,
      locale: Optional[QLocale] = None,
      formatType: QLocale.FormatType = QLocale.FormatType.ShortFormat,
  ) -> str:
    """
    Calls Qt's 'QString QtObject::formatDate(const QDateTime &dateTime, const
    QLocale &locale, QLocale::FormatType formatType) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatDate

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    locale : Optional[QLocale]
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own. May be left out, as in Qt: a new 'QLocale()' is then passed on.

    formatType : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.ShortFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatDate(const QDateTime &dateTime, const QLocale
    #      &locale, QLocale::FormatType formatType) const
    if locale is None:
      locale = QLocale()
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatDateERK9QDateTimeRK7QLocaleNS3_10Format'
        'TypeE',
        self._valueOf(dateTime), self._valueOf(locale), formatType.value,
    )

  @overload(str)
  @overload(str, QLocale)
  @overload(str, QLocale, QLocale.FormatType)
  def formatDate(
      self,
      string: str,
      locale: Optional[QLocale] = None,
      formatType: QLocale.FormatType = QLocale.FormatType.ShortFormat,
  ) -> str:
    """
    Calls Qt's 'QString QtObject::formatDate(const QString &string, const
    QLocale &locale, QLocale::FormatType formatType) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatDate

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    locale : Optional[QLocale]
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own. May be left out, as in Qt: a new 'QLocale()' is then passed on.

    formatType : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.ShortFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatDate(const QString &string, const QLocale
    #      &locale, QLocale::FormatType formatType) const
    if locale is None:
      locale = QLocale()
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatDateERK7QStringRK7QLocaleNS3_10FormatTy'
        'peE',
        string, self._valueOf(locale), formatType.value,
    )

  @overload(QTime, str)
  def formatTime(self, time: QTime, format: str) -> str:
    """
    Calls Qt's 'QString QtObject::formatTime(QTime time, const QString
    &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatTime

    Parameters
    ----------

    time : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatTime(QTime time, const QString &format) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatTimeE5QTimeRK7QString',
        self._valueOf(time), format,
    )

  @overload(QDateTime, str)
  def formatTime(self, dateTime: QDateTime, format: str) -> str:
    """
    Calls Qt's 'QString QtObject::formatTime(const QDateTime &dateTime, const
    QString &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatTime

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatTime(const QDateTime &dateTime, const QString
    #      &format) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatTimeERK9QDateTimeRK7QString',
        self._valueOf(dateTime), format,
    )

  @overload(str, str)
  def formatTime(self, time: str, format: str) -> str:
    """
    Calls Qt's 'QString QtObject::formatTime(const QString &time, const
    QString &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatTime

    Parameters
    ----------

    time : str
      Passed on as it is: a QString is made of it for the call.

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatTime(const QString &time, const QString
    #      &format) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatTimeERK7QStringS2_', time, format,
    )

  @overload(QTime, Qt.DateFormat)
  def formatTime(self, time: QTime, format: Qt.DateFormat) -> str:
    """
    Calls Qt's 'QString QtObject::formatTime(QTime time, Qt::DateFormat
    format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatTime

    Parameters
    ----------

    time : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.

    format : Qt.DateFormat
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatTime(QTime time, Qt::DateFormat format) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatTimeE5QTimeN2Qt10DateFormatE',
        self._valueOf(time), format.value,
    )

  @overload(QDateTime, Qt.DateFormat)
  def formatTime(self, dateTime: QDateTime, format: Qt.DateFormat) -> str:
    """
    Calls Qt's 'QString QtObject::formatTime(const QDateTime &dateTime,
    Qt::DateFormat format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatTime

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    format : Qt.DateFormat
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatTime(const QDateTime &dateTime, Qt::DateFormat
    #      format) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatTimeERK9QDateTimeN2Qt10DateFormatE',
        self._valueOf(dateTime), format.value,
    )

  @overload(str, Qt.DateFormat)
  def formatTime(self, time: str, format: Qt.DateFormat) -> str:
    """
    Calls Qt's 'QString QtObject::formatTime(const QString &time,
    Qt::DateFormat format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatTime

    Parameters
    ----------

    time : str
      Passed on as it is: a QString is made of it for the call.

    format : Qt.DateFormat
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatTime(const QString &time, Qt::DateFormat
    #      format) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatTimeERK7QStringN2Qt10DateFormatE',
        time, format.value,
    )

  @overload(QTime)
  @overload(QTime, QLocale)
  @overload(QTime, QLocale, QLocale.FormatType)
  def formatTime(
      self,
      time: QTime,
      locale: Optional[QLocale] = None,
      formatType: QLocale.FormatType = QLocale.FormatType.ShortFormat,
  ) -> str:
    """
    Calls Qt's 'QString QtObject::formatTime(QTime time, const QLocale
    &locale, QLocale::FormatType formatType) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatTime

    Parameters
    ----------

    time : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.

    locale : Optional[QLocale]
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own. May be left out, as in Qt: a new 'QLocale()' is then passed on.

    formatType : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.ShortFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatTime(QTime time, const QLocale &locale,
    #      QLocale::FormatType formatType) const
    if locale is None:
      locale = QLocale()
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatTimeE5QTimeRK7QLocaleNS1_10FormatTypeE',
        self._valueOf(time), self._valueOf(locale), formatType.value,
    )

  @overload(QDateTime)
  @overload(QDateTime, QLocale)
  @overload(QDateTime, QLocale, QLocale.FormatType)
  def formatTime(
      self,
      dateTime: QDateTime,
      locale: Optional[QLocale] = None,
      formatType: QLocale.FormatType = QLocale.FormatType.ShortFormat,
  ) -> str:
    """
    Calls Qt's 'QString QtObject::formatTime(const QDateTime &dateTime, const
    QLocale &locale, QLocale::FormatType formatType) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatTime

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    locale : Optional[QLocale]
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own. May be left out, as in Qt: a new 'QLocale()' is then passed on.

    formatType : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.ShortFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatTime(const QDateTime &dateTime, const QLocale
    #      &locale, QLocale::FormatType formatType) const
    if locale is None:
      locale = QLocale()
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatTimeERK9QDateTimeRK7QLocaleNS3_10Format'
        'TypeE',
        self._valueOf(dateTime), self._valueOf(locale), formatType.value,
    )

  @overload(str)
  @overload(str, QLocale)
  @overload(str, QLocale, QLocale.FormatType)
  def formatTime(
      self,
      time: str,
      locale: Optional[QLocale] = None,
      formatType: QLocale.FormatType = QLocale.FormatType.ShortFormat,
  ) -> str:
    """
    Calls Qt's 'QString QtObject::formatTime(const QString &time, const
    QLocale &locale, QLocale::FormatType formatType) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatTime

    Parameters
    ----------

    time : str
      Passed on as it is: a QString is made of it for the call.

    locale : Optional[QLocale]
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own. May be left out, as in Qt: a new 'QLocale()' is then passed on.

    formatType : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.ShortFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatTime(const QString &time, const QLocale
    #      &locale, QLocale::FormatType formatType) const
    if locale is None:
      locale = QLocale()
    return self.uglySide.call(
        'ritual_ZNK8QtObject10formatTimeERK7QStringRK7QLocaleNS3_10FormatTy'
        'peE',
        time, self._valueOf(locale), formatType.value,
    )

  @overload(QDateTime, str)
  def formatDateTime(self, date: QDateTime, format: str) -> str:
    """
    Calls Qt's 'QString QtObject::formatDateTime(const QDateTime &date, const
    QString &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatDateTime

    Parameters
    ----------

    date : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatDateTime(const QDateTime &date, const QString
    #      &format) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject14formatDateTimeERK9QDateTimeRK7QString',
        self._valueOf(date), format,
    )

  @overload(str, str)
  def formatDateTime(self, string: str, format: str) -> str:
    """
    Calls Qt's 'QString QtObject::formatDateTime(const QString &string, const
    QString &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatDateTime

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatDateTime(const QString &string, const QString
    #      &format) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject14formatDateTimeERK7QStringS2_', string, format,
    )

  @overload(QDateTime, Qt.DateFormat)
  def formatDateTime(self, date: QDateTime, format: Qt.DateFormat) -> str:
    """
    Calls Qt's 'QString QtObject::formatDateTime(const QDateTime &date,
    Qt::DateFormat format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatDateTime

    Parameters
    ----------

    date : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    format : Qt.DateFormat
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatDateTime(const QDateTime &date, Qt::DateFormat
    #      format) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject14formatDateTimeERK9QDateTimeN2Qt10DateFormatE',
        self._valueOf(date), format.value,
    )

  @overload(str, Qt.DateFormat)
  def formatDateTime(self, string: str, format: Qt.DateFormat) -> str:
    """
    Calls Qt's 'QString QtObject::formatDateTime(const QString &string,
    Qt::DateFormat format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatDateTime

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : Qt.DateFormat
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatDateTime(const QString &string, Qt::DateFormat
    #      format) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject14formatDateTimeERK7QStringN2Qt10DateFormatE',
        string, format.value,
    )

  @overload(QDateTime)
  @overload(QDateTime, QLocale)
  @overload(QDateTime, QLocale, QLocale.FormatType)
  def formatDateTime(
      self,
      date: QDateTime,
      locale: Optional[QLocale] = None,
      formatType: QLocale.FormatType = QLocale.FormatType.ShortFormat,
  ) -> str:
    """
    Calls Qt's 'QString QtObject::formatDateTime(const QDateTime &date, const
    QLocale &locale, QLocale::FormatType formatType) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatDateTime

    Parameters
    ----------

    date : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    locale : Optional[QLocale]
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own. May be left out, as in Qt: a new 'QLocale()' is then passed on.

    formatType : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.ShortFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatDateTime(const QDateTime &date, const QLocale
    #      &locale, QLocale::FormatType formatType) const
    if locale is None:
      locale = QLocale()
    return self.uglySide.call(
        'ritual_ZNK8QtObject14formatDateTimeERK9QDateTimeRK7QLocaleNS3_10Fo'
        'rmatTypeE',
        self._valueOf(date), self._valueOf(locale), formatType.value,
    )

  @overload(str)
  @overload(str, QLocale)
  @overload(str, QLocale, QLocale.FormatType)
  def formatDateTime(
      self,
      string: str,
      locale: Optional[QLocale] = None,
      formatType: QLocale.FormatType = QLocale.FormatType.ShortFormat,
  ) -> str:
    """
    Calls Qt's 'QString QtObject::formatDateTime(const QString &string, const
    QLocale &locale, QLocale::FormatType formatType) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#formatDateTime

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    locale : Optional[QLocale]
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own. May be left out, as in Qt: a new 'QLocale()' is then passed on.

    formatType : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.FormatType.ShortFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::formatDateTime(const QString &string, const QLocale
    #      &locale, QLocale::FormatType formatType) const
    if locale is None:
      locale = QLocale()
    return self.uglySide.call(
        'ritual_ZNK8QtObject14formatDateTimeERK7QStringRK7QLocaleNS3_10Form'
        'atTypeE',
        string, self._valueOf(locale), formatType.value,
    )

  @overload()
  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QtObject::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QtObject::locale() const
    address = self.uglySide.call('ritual_ZNK8QtObject6localeEv')
    return QLocale._cuteOwning(address)

  @overload(str)
  def locale(self, name: str) -> QLocale:
    """
    Calls Qt's 'QLocale QtObject::locale(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#locale

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QtObject::locale(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject6localeERK7QString', name,
    )
    return QLocale._cuteOwning(address)

  @overload(QUrl)
  def url(self, url: QUrl) -> QUrl:
    """
    Calls Qt's 'QUrl QtObject::url(const QUrl &url) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#url

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QtObject::url(const QUrl &url) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject3urlERK4QUrl', self._valueOf(url),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(QUrl)
  def resolvedUrl(self, url: QUrl) -> QUrl:
    """
    Calls Qt's 'QUrl QtObject::resolvedUrl(const QUrl &url) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#resolvedUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QtObject::resolvedUrl(const QUrl &url) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject11resolvedUrlERK4QUrl', self._valueOf(url),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(QUrl, QObject)
  @overload(QUrl, NoneType)
  def resolvedUrl(self, url: QUrl, context: Optional[QObject]) -> QUrl:
    """
    Calls Qt's 'QUrl QtObject::resolvedUrl(const QUrl &url, QObject *context)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#resolvedUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    context : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QtObject::resolvedUrl(const QUrl &url, QObject *context) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject11resolvedUrlERK4QUrlP7QObject',
        self._valueOf(url), self._addressOf(context, 'QObject'),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(QUrl)
  def openUrlExternally(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QtObject::openUrlExternally(const QUrl &url) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#openUrlExternally

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QtObject::openUrlExternally(const QUrl &url) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject17openUrlExternallyERK4QUrl', self._valueOf(url),
    )

  @overload(QJSValue)
  def font(self, fontSpecifier: QJSValue) -> QVariant:
    """
    Calls Qt's 'QVariant QtObject::font(const QJSValue &fontSpecifier)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#font

    Parameters
    ----------

    fontSpecifier : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtObject::font(const QJSValue &fontSpecifier) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject4fontERK8QJSValue', self._valueOf(fontSpecifier),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def fontFamilies(self) -> QStringList:
    """
    Calls Qt's 'QStringList QtObject::fontFamilies() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#fontFamilies

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QtObject::fontFamilies() const
    address = self.uglySide.call('ritual_ZNK8QtObject12fontFamiliesEv')
    return QStringList._cuteOwning(address)

  @overload(str)
  def md5(self, data: str) -> str:
    """
    Calls Qt's 'QString QtObject::md5(const QString &data) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#md5

    Parameters
    ----------

    data : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::md5(const QString &data) const
    return self.uglySide.call('ritual_ZNK8QtObject3md5ERK7QString', data)

  @overload(str)
  def btoa(self, data: str) -> str:
    """
    Calls Qt's 'QString QtObject::btoa(const QString &data) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#btoa

    Parameters
    ----------

    data : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::btoa(const QString &data) const
    return self.uglySide.call('ritual_ZNK8QtObject4btoaERK7QString', data)

  @overload(QByteArray)
  def btoa(self, data: QByteArray) -> QByteArray:
    """
    Calls Qt's 'QByteArray QtObject::btoa(const QByteArray &data) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#btoa

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QtObject::btoa(const QByteArray &data) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject4btoaERK10QByteArray', self._valueOf(data),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QList[QVariant])
  def btoa(self, data: QList[QVariant]) -> QByteArray:
    """
    Calls Qt's 'QByteArray QtObject::btoa(const QVariantList &data) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#btoa

    Parameters
    ----------

    data : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QtObject::btoa(const QVariantList &data) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject4btoaERK5QListI8QVariantE', self._valueOf(data),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(str)
  def atob(self, data: str) -> str:
    """
    Calls Qt's 'QString QtObject::atob(const QString &data) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#atob

    Parameters
    ----------

    data : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::atob(const QString &data) const
    return self.uglySide.call('ritual_ZNK8QtObject4atobERK7QString', data)

  @overload(QByteArray)
  def atob(self, data: QByteArray) -> QByteArray:
    """
    Calls Qt's 'QByteArray QtObject::atob(const QByteArray &data) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#atob

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QtObject::atob(const QByteArray &data) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject4atobERK10QByteArray', self._valueOf(data),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QList[QVariant])
  def atob(self, data: QList[QVariant]) -> QByteArray:
    """
    Calls Qt's 'QByteArray QtObject::atob(const QVariantList &data) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#atob

    Parameters
    ----------

    data : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QtObject::atob(const QVariantList &data) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject4atobERK5QListI8QVariantE', self._valueOf(data),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(str)
  def escapeHtml(self, data: str) -> str:
    """
    Calls Qt's 'QString QtObject::escapeHtml(const QString &data) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#escapeHtml

    Parameters
    ----------

    data : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::escapeHtml(const QString &data) const
    return self.uglySide.call(
        'ritual_ZNK8QtObject10escapeHtmlERK7QString', data,
    )

  @overload(str, QObject, QUrl)
  @overload(str, NoneType, QUrl)
  def createQmlObject(
      self,
      qml: str,
      parent: Optional[QObject],
      url: QUrl,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QtObject::createQmlObject(const QString &qml,
    QObject *parent, const QUrl &url) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#createQmlObject

    Parameters
    ----------

    qml : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QtObject::createQmlObject(const QString &qml, QObject
    #      *parent, const QUrl &url) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject15createQmlObjectERK7QStringP7QObjectRK4QUrl',
        qml, self._addressOf(parent, 'QObject'), self._valueOf(url),
    )
    return QObject._cuteAt(address)

  @overload(QUrl, QObject)
  @overload(QUrl, NoneType)
  def createComponent(
      self,
      url: QUrl,
      parent: Optional[QObject],
  ) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QtObject::createComponent(const QUrl &url,
    QObject *parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#createComponent

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QtObject::createComponent(const QUrl &url, QObject
    #      *parent) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject15createComponentERK4QUrlP7QObject',
        self._valueOf(url), self._addressOf(parent, 'QObject'),
    )
    return QQmlComponent._cuteAt(address)

  @overload(QUrl)
  @overload(QUrl, QQmlComponent.CompilationMode)
  @overload(QUrl, QQmlComponent.CompilationMode, QObject)
  @overload(QUrl, QQmlComponent.CompilationMode, NoneType)
  def createComponent(
      self,
      url: QUrl,
      mode: QQmlComponent.CompilationMode = (
          QQmlComponent.CompilationMode.PreferSynchronous),
      parent: Optional[QObject] = None,
  ) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QtObject::createComponent(const QUrl &url,
    QQmlComponent::CompilationMode mode, QObject *parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#createComponent

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    mode : QQmlComponent.CompilationMode
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlComponent.CompilationMode.PreferSynchronous.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QtObject::createComponent(const QUrl &url,
    #      QQmlComponent::CompilationMode mode, QObject *parent) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject15createComponentERK4QUrlN13QQmlComponent15Comp'
        'ilationModeEP7QObject',
        self._valueOf(url), mode.value, self._addressOf(parent, 'QObject'),
    )
    return QQmlComponent._cuteAt(address)

  @overload(str, str, QObject)
  @overload(str, str, NoneType)
  def createComponent(
      self,
      moduleUri: str,
      typeName: str,
      parent: Optional[QObject],
  ) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QtObject::createComponent(const QString
    &moduleUri, const QString &typeName, QObject *parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#createComponent

    Parameters
    ----------

    moduleUri : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QtObject::createComponent(const QString &moduleUri,
    #      const QString &typeName, QObject *parent) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject15createComponentERK7QStringS2_P7QObject',
        moduleUri, typeName, self._addressOf(parent, 'QObject'),
    )
    return QQmlComponent._cuteAt(address)

  @overload(str, str)
  @overload(str, str, QQmlComponent.CompilationMode)
  @overload(str, str, QQmlComponent.CompilationMode, QObject)
  @overload(str, str, QQmlComponent.CompilationMode, NoneType)
  def createComponent(
      self,
      moduleUri: str,
      typeName: str,
      mode: QQmlComponent.CompilationMode = (
          QQmlComponent.CompilationMode.PreferSynchronous),
      parent: Optional[QObject] = None,
  ) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QtObject::createComponent(const QString
    &moduleUri, const QString &typeName, QQmlComponent::CompilationMode mode,
    QObject *parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#createComponent

    Parameters
    ----------

    moduleUri : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    mode : QQmlComponent.CompilationMode
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlComponent.CompilationMode.PreferSynchronous.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QtObject::createComponent(const QString &moduleUri,
    #      const QString &typeName, QQmlComponent::CompilationMode mode,
    #      QObject *parent) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject15createComponentERK7QStringS2_N13QQmlComponent'
        '15CompilationModeEP7QObject',
        moduleUri, typeName, mode.value, self._addressOf(parent, 'QObject'),
    )
    return QQmlComponent._cuteAt(address)

  @overload(QJSValue)
  def binding(self, function: QJSValue) -> QJSValue:
    """
    Calls Qt's 'QJSValue QtObject::binding(const QJSValue &function) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#binding

    Parameters
    ----------

    function : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QtObject::binding(const QJSValue &function) const
    address = self.uglySide.call(
        'ritual_ZNK8QtObject7bindingERK8QJSValue', self._valueOf(function),
    )
    from . import QJSValue
    return QJSValue._cuteOwning(address)

  def uiLanguage(self) -> str:
    """
    Calls Qt's 'QString QtObject::uiLanguage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#uiLanguage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtObject::uiLanguage() const
    return self.uglySide.call('ritual_ZNK8QtObject10uiLanguageEv')

  def inputMethod(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QtObject::inputMethod() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#inputMethod

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QtObject::inputMethod() const
    address = self.uglySide.call('ritual_ZNK8QtObject11inputMethodEv')
    return QObject._cuteAt(address)

  def styleHints(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QtObject::styleHints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#styleHints

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QtObject::styleHints() const
    address = self.uglySide.call('ritual_ZNK8QtObject10styleHintsEv')
    return QObject._cuteAt(address)

  def qmlEngine(self) -> Optional[QQmlEngine]:
    """
    Calls Qt's 'QQmlEngine *QtObject::qmlEngine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#qmlEngine

    Returns
    -------

    Optional[QQmlEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEngine *QtObject::qmlEngine() const
    address = self.uglySide.call('ritual_ZNK8QtObject9qmlEngineEv')
    from . import QQmlEngine
    return QQmlEngine._cuteAt(address)

  def jsEngine(self) -> Optional[QJSEngine]:
    """
    Calls Qt's 'QJSEngine *QtObject::jsEngine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#jsEngine

    Returns
    -------

    Optional[QJSEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QJSEngine *QtObject::jsEngine() const
    address = self.uglySide.call('ritual_ZNK8QtObject8jsEngineEv')
    from . import QJSEngine
    return QJSEngine._cuteAt(address)

  def v4Engine(self) -> Optional[QV4.ExecutionEngine]:
    """
    Calls Qt's 'QV4::ExecutionEngine *QtObject::v4Engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#v4Engine

    Returns
    -------

    Optional[QV4.ExecutionEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::ExecutionEngine *QtObject::v4Engine() const
    address = self.uglySide.call('ritual_ZNK8QtObject8v4EngineEv')
    return QV4.ExecutionEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setUiLanguage(self, uiLanguage: str) -> None:
    """
    Calls Qt's 'void QtObject::setUiLanguage(const QString &uiLanguage)'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#setUiLanguage

    Parameters
    ----------

    uiLanguage : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtObject::setUiLanguage(const QString &uiLanguage)
    self.uglySide.call(
        'ritual_ZN8QtObject13setUiLanguageERK7QString', uiLanguage,
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

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def __init__(self, engine: Optional[QV4.ExecutionEngine]) -> None:
    """
    Notes what was given, for Qt's 'QtObject::QtObject(QV4::ExecutionEngine
    *engine)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#QtObject

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtObject::QtObject(QV4::ExecutionEngine *engine)
    self._noteCreation(QtObject, lambda: Rituals.call(
        'ritual_ZN8QtObjectC1EPN3QV415ExecutionEngineE',
        self._addressOf(engine),
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

  def quit(self) -> None:
    """
    Calls Qt's 'void QtObject::quit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#quit
    """
    #  void QtObject::quit() const
    self.uglySide.call('ritual_ZNK8QtObject4quitEv')

  @overload(int)
  def exit(self, retCode: int) -> None:
    """
    Calls Qt's 'void QtObject::exit(int retCode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#exit

    Parameters
    ----------

    retCode : int
      Passed on as it is.
    """
    #  void QtObject::exit(int retCode) const
    self.uglySide.call('ritual_ZNK8QtObject4exitEi', retCode)

  @overload(QQmlV4Function)
  @overload(NoneType)
  def callLater(self, args: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QtObject::callLater(QQmlV4FunctionPtr args)'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#callLater

    Parameters
    ----------

    args : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtObject::callLater(QQmlV4FunctionPtr args)
    self.uglySide.call(
        'ritual_ZN8QtObject9callLaterEP14QQmlV4Function',
        self._addressOf(args),
    )

  def uiLanguageChanged(self) -> None:
    """
    Calls Qt's 'void QtObject::uiLanguageChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#uiLanguageChanged
    """
    #  void QtObject::uiLanguageChanged()
    self.uglySide.call('ritual_ZN8QtObject17uiLanguageChangedEv')

  def platform(self) -> Optional[QQmlPlatform]:
    """
    Calls Qt's 'QQmlPlatform *QtObject::platform()'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#platform

    Returns
    -------

    Optional[QQmlPlatform]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlPlatform *QtObject::platform()
    address = self.uglySide.call('ritual_ZN8QtObject8platformEv')
    from . import QQmlPlatform
    return QQmlPlatform._cuteAt(address)

  def application(self) -> Optional[QQmlApplication]:
    """
    Calls Qt's 'QQmlApplication *QtObject::application()'.

    Qt's own words: https://doc.qt.io/qt-6/qtobject.html#application

    Returns
    -------

    Optional[QQmlApplication]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlApplication *QtObject::application()
    address = self.uglySide.call('ritual_ZN8QtObject11applicationEv')
    from . import QQmlApplication
    return QQmlApplication._cuteAt(address)

  @staticmethod
  def enumStringToValue(*__, **_) -> Never:
    """
    Qt's 'double QtObject::enumStringToValue(const QJSManagedValue &enumType,
    const QString &string)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtObject.enumStringToValue' has no cute function yet. Qt's "
        "'double QtObject::enumStringToValue(const QJSManagedValue "
        "&enumType, const QString &string)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def enumValueToString(*__, **_) -> Never:
    """
    Qt's 'QString QtObject::enumValueToString(const QJSManagedValue
    &enumType, double value)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QtObject.enumValueToString' has no cute function yet. Qt's "
        "'QString QtObject::enumValueToString(const QJSManagedValue "
        "&enumType, double value)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def enumValueToStrings(*__, **_) -> Never:
    """
    Qt's 'QStringList QtObject::enumValueToStrings(const QJSManagedValue
    &enumType, double value)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QtObject.enumValueToStrings' has no cute function yet. Qt's "
        "'QStringList QtObject::enumValueToStrings(const QJSManagedValue "
        "&enumType, double value)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def getContexts(*__, **_) -> Never:
    """
    Qt's 'Contexts QtObject::getContexts() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QtObject.getContexts' has no cute function yet. Qt's 'Contexts "
        "QtObject::getContexts() const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def retrieveFromEnum(*__, **_) -> Never:
    """
    Qt's 'QtObject::retrieveFromEnum': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QtObject.retrieveFromEnum' has no cute function yet. Qt's "
        "'QtObject::retrieveFromEnum': a template: a pattern and no single "
        "function.")

  @staticmethod
  def uiLanguageBindable(*__, **_) -> Never:
    """
    Qt's 'QBindable<QString> QtObject::uiLanguageBindable()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtObject.uiLanguageBindable' has no cute function yet. Qt's "
        "'QBindable<QString> QtObject::uiLanguageBindable()': gives a type "
        "Python has no way to take yet.")
