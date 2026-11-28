"""
QQuickShaderEffectMesh binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickshadereffectmesh_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickShaderEffectMesh to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF
  from . import QSGGeometry
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSGGeometry = WAIT['QSGGeometry']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShaderEffectMesh(QObject):
  """
  The cute side of Qt's QQuickShaderEffectMesh: a plain Python object
  standing in front of one C++ QQuickShaderEffectMesh.

  It is built on the cute 'QObject', as Qt's QQuickShaderEffectMesh is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickShaderEffectMesh that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr',
  'updateGeometry', 'log', 'geometryChanged'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickShaderEffectMesh::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickShaderEffectMesh::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickShaderEffectMesh::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'bool QQuickShaderEffectMesh::validateAttributes(const
    QList<QByteArray> &attributes, int *posIndex)': takes a number to change
    where it is.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 not a gap; 2 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QQuickShaderEffectMesh is created at the first use, not by
    'QQuickShaderEffectMesh(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShaderEffectMesh.
  - Qt tells when it has removed the C++ QQuickShaderEffectMesh. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickShaderEffectMesh that has no cute function yet,
    '__init__', 'validateAttributes', holds a function that raises
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
    Calls Qt's 'QString QQuickShaderEffectMesh::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshadereffectmesh.html#tr

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
    #  QString QQuickShaderEffectMesh::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQuickShaderEffectMesh2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShaderEffectMesh'

  #  A C++ QQuickShaderEffectMesh Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickShaderEffectMesh'

  #  The functions Qt calls itself that QQuickShaderEffectMesh is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'validateAttributes': (
          'bool QQuickShaderEffectMesh::validateAttributes(const '
          'QList<QByteArray> &, int *)',
      ),
  }

  #  The functions Qt calls itself that QQuickShaderEffectMesh is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'updateGeometry': (
          ('_ZN22QQuickShaderEffectMesh14updateGeometryEP11QSGGeometryiiRK6'
           'QRectFS4_',
           ('address', 'address', 'QtQuick:QSGGeometry'),
           (
               ('address', 'address', 'QtQuick:QSGGeometry'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'log': (
          ('_ZNK22QQuickShaderEffectMesh3logEv',
           ('address', 'text', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *QQuickShaderEffectMesh::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectmesh.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickShaderEffectMesh::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickShaderEffectMesh10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def log(self) -> str:
    """
    Calls Qt's 'QString QQuickShaderEffectMesh::log() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshadereffectmesh.html#log

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickShaderEffectMesh::log() const
    ritual = 'ritual_ZNK22QQuickShaderEffectMesh3logEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickShaderEffectMesh3logEv'
    return self.uglySide.call(ritual)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QQuickShaderEffectMesh::QQuickShaderEffectMesh(QObject *parent)':
      the class is abstract, so C++ cannot make one, and the C++ class of
      ours does not fill in every function it leaves open.
    - Qt's 'QQuickShaderEffectMesh::QQuickShaderEffectMesh(QObjectPrivate
      &dd, QObject *parent)': the class is abstract, so C++ cannot make one,
      and the C++ class of ours does not fill in every function it leaves
      open.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectMesh.__init__' has no cute function yet. Qt's "
        "'QQuickShaderEffectMesh::QQuickShaderEffectMesh(QObject *parent)': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open. Qt's "
        "'QQuickShaderEffectMesh::QQuickShaderEffectMesh(QObjectPrivate "
        "&dd, QObject *parent)': the class is abstract, so C++ cannot make "
        "one, and the C++ class of ours does not fill in every function it "
        "leaves open.")

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

  @overload(QSGGeometry, int, int, QRectF, QRectF)
  @overload(NoneType, int, int, QRectF, QRectF)
  def updateGeometry(
      self,
      geometry: Optional[QSGGeometry],
      attrCount: int,
      posIndex: int,
      srcRect: QRectF,
      rect: QRectF,
  ) -> Optional[QSGGeometry]:
    """
    Calls Qt's 'QSGGeometry
    *QQuickShaderEffectMesh::updateGeometry(QSGGeometry *geometry, int
    attrCount, int posIndex, const QRectF &srcRect, const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectmesh.html#updateGeometry

    Parameters
    ----------

    geometry : Optional[QSGGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    attrCount : int
      Passed on as it is.

    posIndex : int
      Passed on as it is.

    srcRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    Optional[QSGGeometry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGGeometry *QQuickShaderEffectMesh::updateGeometry(QSGGeometry
    #      *geometry, int attrCount, int posIndex, const QRectF &srcRect,
    #      const QRectF &rect)
    address = self.uglySide.call(
        'ritual_ZN22QQuickShaderEffectMesh14updateGeometryEP11QSGGeometryii'
        'RK6QRectFS4_',
        self._addressOf(geometry), attrCount, posIndex,
        self._valueOf(srcRect), self._valueOf(rect),
    )
    from . import QSGGeometry
    return QSGGeometry._cuteAt(address)

  def geometryChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectMesh::geometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectmesh.html#geometryChanged
    """
    #  void QQuickShaderEffectMesh::geometryChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickShaderEffectMesh15geometryChangedEv',
    )

  @staticmethod
  def validateAttributes(*__, **_) -> Never:
    """
    Qt's 'bool QQuickShaderEffectMesh::validateAttributes(const
    QList<QByteArray> &attributes, int *posIndex)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectMesh.validateAttributes' has no cute function "
        "yet. Qt's 'bool QQuickShaderEffectMesh::validateAttributes(const "
        "QList<QByteArray> &attributes, int *posIndex)': takes a number to "
        "change where it is.")
