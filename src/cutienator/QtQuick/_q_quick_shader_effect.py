"""
QQuickShaderEffect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickshadereffect_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickShaderEffect to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QEvent, QMetaObject, QRectF, QUrl
  from ..QtCore import QVariant
  from . import QQuickShaderEffectPrivate, QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QEvent = WAIT['QEvent']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShaderEffect(QQuickItem):
  """
  The cute side of Qt's QQuickShaderEffect: a plain Python object standing in
  front of one C++ QQuickShaderEffect.

  It is built on the cute 'QQuickItem', as Qt's QQuickShaderEffect is built
  on Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickShaderEffect that has a ritual and that Python
  can call so far, 32 names in all: 'metaObject', 'tr', 'fragmentShader',
  'setFragmentShader', 'vertexShader', 'setVertexShader', 'blending',
  'setBlending', 'mesh', 'setMesh', 'cullMode', 'setCullMode',
  'supportsAtlasTextures', 'setSupportsAtlasTextures', 'log', 'status',
  'isComponentComplete', 'updateUniformValue', 'fragmentShaderChanged',
  'vertexShaderChanged', 'blendingChanged', 'meshChanged', 'cullModeChanged',
  'logChanged', 'statusChanged', 'supportsAtlasTexturesChanged', 'event',
  'geometryChange', 'updatePaintNode', 'componentComplete', 'itemChange',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickShaderEffect::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickShaderEffect::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickShaderEffect::~QQuickShaderEffect()': the destructor: Python
    never removes a C++ QQuickShaderEffect.
  - Qt's 'const QQuickShaderEffectPrivate *QQuickShaderEffect::d_func()
    const': takes in Python what 'QQuickShaderEffectPrivate
    *QQuickShaderEffect::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 39 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickShaderEffect is created at the first use, not by
    'QQuickShaderEffect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShaderEffect.
  - Qt tells when it has removed the C++ QQuickShaderEffect. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickShaderEffect, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class CullMode(CuteNum):
    """
    The enum 'QQuickShaderEffect::CullMode' of Qt, with the 3 names Qt gives
    in it.
    """

    NoCulling = Kee[int](0)
    BackFaceCulling = Kee[int](1)
    FrontFaceCulling = Kee[int](2)

  class Status(CuteNum):
    """
    The enum 'QQuickShaderEffect::Status' of Qt, with the 3 names Qt gives in
    it.
    """

    Compiled = Kee[int](0)
    Uncompiled = Kee[int](1)
    Error = Kee[int](2)

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
    Calls Qt's 'QString QQuickShaderEffect::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshadereffect.html#tr

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
    #  QString QQuickShaderEffect::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickShaderEffect2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShaderEffect'

  #  A C++ QQuickShaderEffect Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickShaderEffect'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickShaderEffect::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshadereffect.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickShaderEffect::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickShaderEffect10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fragmentShader(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickShaderEffect::fragmentShader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#fragmentShader

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickShaderEffect::fragmentShader() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickShaderEffect14fragmentShaderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def vertexShader(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickShaderEffect::vertexShader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#vertexShader

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickShaderEffect::vertexShader() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickShaderEffect12vertexShaderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def blending(self) -> bool:
    """
    Calls Qt's 'bool QQuickShaderEffect::blending() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshadereffect.html#blending
    """
    #  bool QQuickShaderEffect::blending() const
    return self.uglySide.call('ritual_ZNK18QQuickShaderEffect8blendingEv')

  def mesh(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickShaderEffect::mesh() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshadereffect.html#mesh

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickShaderEffect::mesh() const
    address = self.uglySide.call('ritual_ZNK18QQuickShaderEffect4meshEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def cullMode(self) -> CullMode:
    """
    Calls Qt's 'CullMode QQuickShaderEffect::cullMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshadereffect.html#cullMode

    Returns
    -------

    CullMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CullMode(number)' gives.
    """
    #  CullMode QQuickShaderEffect::cullMode() const
    return QQuickShaderEffect.CullMode(self.uglySide.call(
        'ritual_ZNK18QQuickShaderEffect8cullModeEv',
    ))

  def supportsAtlasTextures(self) -> bool:
    """
    Calls Qt's 'bool QQuickShaderEffect::supportsAtlasTextures() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#supportsAtlasTextures
    """
    #  bool QQuickShaderEffect::supportsAtlasTextures() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickShaderEffect21supportsAtlasTexturesEv',
    )

  def log(self) -> str:
    """
    Calls Qt's 'QString QQuickShaderEffect::log() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshadereffect.html#log

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickShaderEffect::log() const
    return self.uglySide.call('ritual_ZNK18QQuickShaderEffect3logEv')

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQuickShaderEffect::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshadereffect.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQuickShaderEffect::status() const
    return QQuickShaderEffect.Status(self.uglySide.call(
        'ritual_ZNK18QQuickShaderEffect6statusEv',
    ))

  def isComponentComplete(self) -> bool:
    """
    Calls Qt's 'bool QQuickShaderEffect::isComponentComplete() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#isComponentComplete
    """
    #  bool QQuickShaderEffect::isComponentComplete() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickShaderEffect19isComponentCompleteEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setFragmentShader(self, fileUrl: QUrl) -> None:
    """
    Calls Qt's 'void QQuickShaderEffect::setFragmentShader(const QUrl
    &fileUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#setFragmentShader

    Parameters
    ----------

    fileUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickShaderEffect::setFragmentShader(const QUrl &fileUrl)
    self.uglySide.call(
        'ritual_ZN18QQuickShaderEffect17setFragmentShaderERK4QUrl',
        self._valueOf(fileUrl),
    )

  @overload(QUrl)
  def setVertexShader(self, fileUrl: QUrl) -> None:
    """
    Calls Qt's 'void QQuickShaderEffect::setVertexShader(const QUrl
    &fileUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#setVertexShader

    Parameters
    ----------

    fileUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickShaderEffect::setVertexShader(const QUrl &fileUrl)
    self.uglySide.call(
        'ritual_ZN18QQuickShaderEffect15setVertexShaderERK4QUrl',
        self._valueOf(fileUrl),
    )

  @overload(bool)
  def setBlending(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickShaderEffect::setBlending(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#setBlending

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickShaderEffect::setBlending(bool enable)
    self.uglySide.call(
        'ritual_ZN18QQuickShaderEffect11setBlendingEb', enable,
    )

  @overload(QVariant)
  def setMesh(self, mesh: QVariant) -> None:
    """
    Calls Qt's 'void QQuickShaderEffect::setMesh(const QVariant &mesh)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshadereffect.html#setMesh

    Parameters
    ----------

    mesh : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickShaderEffect::setMesh(const QVariant &mesh)
    self.uglySide.call(
        'ritual_ZN18QQuickShaderEffect7setMeshERK8QVariant',
        self._valueOf(mesh),
    )

  @overload(CullMode)
  def setCullMode(self, face: CullMode) -> None:
    """
    Calls Qt's 'void QQuickShaderEffect::setCullMode(CullMode face)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#setCullMode

    Parameters
    ----------

    face : CullMode
      Passed on as its number.
    """
    #  void QQuickShaderEffect::setCullMode(CullMode face)
    self.uglySide.call(
        'ritual_ZN18QQuickShaderEffect11setCullModeENS_8CullModeE',
        face.value,
    )

  @overload(bool)
  def setSupportsAtlasTextures(self, supports: bool) -> None:
    """
    Calls Qt's 'void QQuickShaderEffect::setSupportsAtlasTextures(bool
    supports)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#setSupportsAtlasTextures

    Parameters
    ----------

    supports : bool
      Passed on as it is.
    """
    #  void QQuickShaderEffect::setSupportsAtlasTextures(bool supports)
    self.uglySide.call(
        'ritual_ZN18QQuickShaderEffect24setSupportsAtlasTexturesEb',
        supports,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickShaderEffect::QQuickShaderEffect(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#QQuickShaderEffect

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickShaderEffect::QQuickShaderEffect(QQuickItem *parent)
    self._noteCreation(QQuickShaderEffect, lambda: Rituals.call(
        'ritual_ZN18QQuickShaderEffectC1EP10QQuickItem',
        self._addressOf(parent),
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

  @overload(QByteArray, QVariant)
  def updateUniformValue(self, name: QByteArray, value: QVariant) -> bool:
    """
    Calls Qt's 'bool QQuickShaderEffect::updateUniformValue(const QByteArray
    &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#updateUniformValue

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QQuickShaderEffect::updateUniformValue(const QByteArray &name,
    #      const QVariant &value)
    return self.uglySide.call(
        'ritual_ZN18QQuickShaderEffect18updateUniformValueERK10QByteArrayRK'
        '8QVariant',
        self._valueOf(name), self._valueOf(value),
    )

  def fragmentShaderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffect::fragmentShaderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#fragmentShaderChanged
    """
    #  void QQuickShaderEffect::fragmentShaderChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickShaderEffect21fragmentShaderChangedEv',
    )

  def vertexShaderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffect::vertexShaderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#vertexShaderChanged
    """
    #  void QQuickShaderEffect::vertexShaderChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickShaderEffect19vertexShaderChangedEv',
    )

  def blendingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffect::blendingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#blendingChanged
    """
    #  void QQuickShaderEffect::blendingChanged()
    self.uglySide.call('ritual_ZN18QQuickShaderEffect15blendingChangedEv')

  def meshChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffect::meshChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#meshChanged
    """
    #  void QQuickShaderEffect::meshChanged()
    self.uglySide.call('ritual_ZN18QQuickShaderEffect11meshChangedEv')

  def cullModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffect::cullModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#cullModeChanged
    """
    #  void QQuickShaderEffect::cullModeChanged()
    self.uglySide.call('ritual_ZN18QQuickShaderEffect15cullModeChangedEv')

  def logChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffect::logChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshadereffect.html#logChanged
    """
    #  void QQuickShaderEffect::logChanged()
    self.uglySide.call('ritual_ZN18QQuickShaderEffect10logChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffect::statusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#statusChanged
    """
    #  void QQuickShaderEffect::statusChanged()
    self.uglySide.call('ritual_ZN18QQuickShaderEffect13statusChangedEv')

  def supportsAtlasTexturesChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffect::supportsAtlasTexturesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html
    """
    #  void QQuickShaderEffect::supportsAtlasTexturesChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickShaderEffect28supportsAtlasTexturesChangedEv',
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickShaderEffect::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshadereffect.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickShaderEffect::event(QEvent *e)
    ritual = 'ritual_ZN18QQuickShaderEffect5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickShaderEffect5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickShaderEffect::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickShaderEffect::geometryChange(const QRectF &newGeometry,
    #      const QRectF &oldGeometry)
    ritual = 'ritual_ZN18QQuickShaderEffect14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickShaderEffect14geometryChangeERK6QRectFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      oldNode: Optional[QSGNode],
      updatePaintNodeData: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickShaderEffect::updatePaintNode(QSGNode
    *oldNode, UpdatePaintNodeData *updatePaintNodeData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#updatePaintNode

    Parameters
    ----------

    oldNode : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    updatePaintNodeData : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickShaderEffect::updatePaintNode(QSGNode *oldNode,
    #      UpdatePaintNodeData *updatePaintNodeData)
    ritual = (
        'ritual_ZN18QQuickShaderEffect15updatePaintNodeEP7QSGNodePN10QQuick'
        'Item19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickShaderEffect15updatePaintNodeEP7QSGNodePN10'
          'QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual,
        self._addressOf(oldNode, 'QSGNode'),
        self._addressOf(updatePaintNodeData),
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffect::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffect.html#componentComplete
    """
    #  void QQuickShaderEffect::componentComplete()
    ritual = 'ritual_ZN18QQuickShaderEffect17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickShaderEffect17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickShaderEffect::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshadereffect.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickShaderEffect::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN18QQuickShaderEffect10itemChangeEN10QQuickItem10ItemChang'
        'eERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickShaderEffect10itemChangeEN10QQuickItem10Ite'
          'mChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  def d_func(self) -> Optional[QQuickShaderEffectPrivate]:
    """
    Calls Qt's 'QQuickShaderEffectPrivate *QQuickShaderEffect::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshadereffect.html#d_func

    Returns
    -------

    Optional[QQuickShaderEffectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShaderEffectPrivate *QQuickShaderEffect::d_func()
    address = self.uglySide.call('ritual_ZN18QQuickShaderEffect6d_funcEv')
    from . import QQuickShaderEffectPrivate
    return QQuickShaderEffectPrivate._cuteAt(address)
