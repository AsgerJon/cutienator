"""
QQuick3DQuadTextureProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qquick3dquadtextureprovider_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DQuadTextureProvider to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtQuick3D import QQuick3DPropertyChangedTracker, QQuick3DTextureData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QMetaProperty, QUrl
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaProperty = WAIT['QMetaProperty']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DQuadTextureProvider(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DQuadTextureProvider: a plain Python object
  standing in front of one C++ QQuick3DQuadTextureProvider.

  What exists
  -----------

  Every function of Qt's QQuick3DQuadTextureProvider that has a ritual and
  that Python can call so far, 13 names in all: 'metaObject',
  'fragmentShader', 'fragmentShaderCode', 'width', 'height', 'format',
  'fragmentShaderChanged', 'fragmentShaderCodeChanged', 'widthChanged',
  'heightChanged', 'formatChanged', 'updateSpatialNode',
  'markTrackedPropertyDirty'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DQuadTextureProvider::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuick3DQuadTextureProvider::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DQuadTextureProvider::~QQuick3DQuadTextureProvider()': the
    destructor: Python never removes a C++ QQuick3DQuadTextureProvider.
  - Qt's 'void QQuick3DQuadTextureProvider::markDirty(Dirty v)': names the
    enum 'QQuick3DQuadTextureProvider::Dirty', whose class cannot be named
    here.

  What has no ritual
  ------------------

  9 of the 26 functions Qt declares: 7 leans on 'QQuick3DQuadTextureProvider;
  2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DQuadTextureProvider is created at the first use, not by
    'QQuick3DQuadTextureProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DQuadTextureProvider.
  - Qt tells when it has removed the C++ QQuick3DQuadTextureProvider. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DQuadTextureProvider that has no cute function
    yet, '__init__', 'markDirty', 'setFormat', 'setFragmentShader',
    'setFragmentShaderCode', 'setHeight', 'setWidth', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DQuadTextureProvider'

  #  A C++ QQuick3DQuadTextureProvider Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DQuadTextureProvider'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DQuadTextureProvider::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquadtextureprovider.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DQuadTextureProvider::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuick3DQuadTextureProvider10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fragmentShader(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuick3DQuadTextureProvider::fragmentShader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquadtextureprovider.html#fragmentShader

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuick3DQuadTextureProvider::fragmentShader() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuick3DQuadTextureProvider14fragmentShaderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def fragmentShaderCode(self) -> str:
    """
    Calls Qt's 'QString QQuick3DQuadTextureProvider::fragmentShaderCode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquadtextureprovider.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DQuadTextureProvider::fragmentShaderCode() const
    return self.uglySide.call(
        'ritual_ZNK27QQuick3DQuadTextureProvider18fragmentShaderCodeEv',
    )

  def width(self) -> int:
    """
    Calls Qt's 'int QQuick3DQuadTextureProvider::width() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquadtextureprovider.html#width
    """
    #  int QQuick3DQuadTextureProvider::width() const
    return self.uglySide.call(
        'ritual_ZNK27QQuick3DQuadTextureProvider5widthEv',
    )

  def height(self) -> int:
    """
    Calls Qt's 'int QQuick3DQuadTextureProvider::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquadtextureprovider.html#height
    """
    #  int QQuick3DQuadTextureProvider::height() const
    return self.uglySide.call(
        'ritual_ZNK27QQuick3DQuadTextureProvider6heightEv',
    )

  def format(self) -> QQuick3DTextureData.Format:
    """
    Calls Qt's 'QQuick3DTextureData::Format
    QQuick3DQuadTextureProvider::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquadtextureprovider.html#format

    Returns
    -------

    QQuick3DTextureData.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DTextureData.Format(number)' gives.
    """
    #  QQuick3DTextureData::Format QQuick3DQuadTextureProvider::format()
    #      const
    return QQuick3DTextureData.Format(self.uglySide.call(
        'ritual_ZNK27QQuick3DQuadTextureProvider6formatEv',
    ))

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
    Qt's
    'QQuick3DQuadTextureProvider::QQuick3DQuadTextureProvider(QQuick3DObject
    *parent)': leans on
    'QQuick3DQuadTextureProvider::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DQuadTextureProvider.__init__' has no cute function yet. "
        "Qt's "
        "'QQuick3DQuadTextureProvider::QQuick3DQuadTextureProvider(QQuick3DO"
        "bject *parent)': leans on "
        "'QQuick3DQuadTextureProvider::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def fragmentShaderChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DQuadTextureProvider::fragmentShaderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquadtextureprovider.html
    """
    #  void QQuick3DQuadTextureProvider::fragmentShaderChanged()
    self.uglySide.call(
        'ritual_ZN27QQuick3DQuadTextureProvider21fragmentShaderChangedEv',
    )

  def fragmentShaderCodeChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DQuadTextureProvider::fragmentShaderCodeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquadtextureprovider.html
    """
    #  void QQuick3DQuadTextureProvider::fragmentShaderCodeChanged()
    self.uglySide.call(
        'ritual_ZN27QQuick3DQuadTextureProvider25fragmentShaderCodeChangedE'
        'v',
    )

  def widthChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DQuadTextureProvider::widthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquadtextureprovider.html#widthChanged
    """
    #  void QQuick3DQuadTextureProvider::widthChanged()
    self.uglySide.call(
        'ritual_ZN27QQuick3DQuadTextureProvider12widthChangedEv',
    )

  def heightChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DQuadTextureProvider::heightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquadtextureprovider.html#heightChanged
    """
    #  void QQuick3DQuadTextureProvider::heightChanged()
    self.uglySide.call(
        'ritual_ZN27QQuick3DQuadTextureProvider13heightChangedEv',
    )

  def formatChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DQuadTextureProvider::formatChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquadtextureprovider.html#formatChanged
    """
    #  void QQuick3DQuadTextureProvider::formatChanged()
    self.uglySide.call(
        'ritual_ZN27QQuick3DQuadTextureProvider13formatChangedEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DQuadTextureProvider::updateSpatialNode(QSSGRenderGraphObject
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquadtextureprovider.html#updateSpatialNode

    Parameters
    ----------

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject *QQuick3DQuadTextureProvider::updateSpatialNode(
    #      QSSGRenderGraphObject *node)
    address = self.uglySide.call(
        'ritual_ZN27QQuick3DQuadTextureProvider17updateSpatialNodeEP21QSSGR'
        'enderGraphObject',
        self._addressOf(node),
    )
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  @overload(QMetaProperty, QQuick3DPropertyChangedTracker.DirtyPropertyHint)
  def markTrackedPropertyDirty(
      self,
      property: QMetaProperty,
      hint: QQuick3DPropertyChangedTracker.DirtyPropertyHint,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DQuadTextureProvider::markTrackedPropertyDirty(QMetaProperty
    property, DirtyPropertyHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquadtextureprovider.html

    Parameters
    ----------

    property : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.

    hint : QQuick3DPropertyChangedTracker.DirtyPropertyHint
      Passed on as its number.
    """
    #  void QQuick3DQuadTextureProvider::markTrackedPropertyDirty(
    #      QMetaProperty property, DirtyPropertyHint hint)
    ritual = (
        'ritual_ZN27QQuick3DQuadTextureProvider24markTrackedPropertyDirtyE1'
        '3QMetaPropertyN30QQuick3DPropertyChangedTracker17DirtyPropertyHint'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuick3DQuadTextureProvider24markTrackedPropertyD'
          'irtyE13QMetaPropertyN30QQuick3DPropertyChangedTracker17DirtyProp'
          'ertyHintE')
    self.uglySide.call(ritual, self._valueOf(property), hint.value)

  @staticmethod
  def markDirty(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DQuadTextureProvider::markDirty(Dirty v)': names the
    enum 'QQuick3DQuadTextureProvider::Dirty', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QQuick3DQuadTextureProvider.markDirty' has no cute function yet. "
        "Qt's 'void QQuick3DQuadTextureProvider::markDirty(Dirty v)': names "
        "the enum 'QQuick3DQuadTextureProvider::Dirty', whose class cannot "
        "be named here.")

  @staticmethod
  def setFormat(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DQuadTextureProvider::setFormat(QQuick3DTextureData::Format
    newFormat)': leans on 'QQuick3DQuadTextureProvider::formatChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DQuadTextureProvider.setFormat' has no cute function yet. "
        "Qt's 'void "
        "QQuick3DQuadTextureProvider::setFormat(QQuick3DTextureData::Format "
        "newFormat)': leans on "
        "'QQuick3DQuadTextureProvider::formatChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setFragmentShader(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DQuadTextureProvider::setFragmentShader(const QUrl
    &newFragmentShader)': leans on
    'QQuick3DQuadTextureProvider::fragmentShaderChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuick3DQuadTextureProvider.setFragmentShader' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DQuadTextureProvider::setFragmentShader(const QUrl "
        "&newFragmentShader)': leans on "
        "'QQuick3DQuadTextureProvider::fragmentShaderChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setFragmentShaderCode(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DQuadTextureProvider::setFragmentShaderCode(const
    QString &newFragmentShaderCode)': leans on
    'QQuick3DQuadTextureProvider::fragmentShaderCodeChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DQuadTextureProvider.setFragmentShaderCode' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DQuadTextureProvider::setFragmentShaderCode(const QString "
        "&newFragmentShaderCode)': leans on "
        "'QQuick3DQuadTextureProvider::fragmentShaderCodeChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setHeight(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DQuadTextureProvider::setHeight(int newHeight)': leans
    on 'QQuick3DQuadTextureProvider::heightChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DQuadTextureProvider.setHeight' has no cute function yet. "
        "Qt's 'void QQuick3DQuadTextureProvider::setHeight(int newHeight)': "
        "leans on 'QQuick3DQuadTextureProvider::heightChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setWidth(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DQuadTextureProvider::setWidth(int newWidth)': leans on
    'QQuick3DQuadTextureProvider::widthChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DQuadTextureProvider.setWidth' has no cute function yet. "
        "Qt's 'void QQuick3DQuadTextureProvider::setWidth(int newWidth)': "
        "leans on 'QQuick3DQuadTextureProvider::widthChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
