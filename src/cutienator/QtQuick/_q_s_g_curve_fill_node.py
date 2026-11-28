"""
QSGCurveFillNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgcurvefillnode_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGCurveFillNode to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QGradient
from . import QSGCurveAbstractNode, QSGGeometry, QSGGradientCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QVector2D, QVector3D
  from . import QSGTextureProvider, QSGTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QSGTextureProvider = WAIT['QSGTextureProvider']
  QSGTransform = WAIT['QSGTransform']
  QVector2D = WAIT['QVector2D']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGCurveFillNode(QObject, QSGCurveAbstractNode):
  """
  The cute side of Qt's QSGCurveFillNode: a plain Python object standing in
  front of one C++ QSGCurveFillNode.

  It is built on the cute 'QObject', as Qt's QSGCurveFillNode is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QSGCurveAbstractNode' as well, as Qt's QSGCurveFillNode is built on Qt's
  QSGCurveAbstractNode too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGCurveFillNode that has a ritual and that Python
  can call so far, 26 names in all: 'metaObject', 'tr', 'setColor', 'color',
  'setFillTextureProvider', 'fillTextureProvider', 'setFillGradient',
  'fillGradient', 'setGradientType', 'gradientType', 'setFillTransform',
  'fillTransform', 'debug', 'setDebug', 'appendTriangle', 'cookGeometry',
  'reserve', 'preprocess', 'boundsSize', 'setBoundsSize',
  'useStandardDerivatives', 'setUseStandardDerivatives',
  'handleTextureChanged', 'handleTextureProviderDestroyed', 'updateMaterial',
  'attributes'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGCurveFillNode::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QSGCurveFillNode::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QSGCurveFillNode::appendTriangle(const std::array<QVector2D,
    3> &v, const std::array<QVector2D, 3> &n, std::function<QVector3D
    (QVector2D)> uvForPoint)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSGCurveFillNode::appendTriangle(const QVector2D &v1, const
    QVector2D &v2, const QVector2D &v3, std::function<QVector3D (QVector2D)>
    uvForPoint)': takes a type Python has no way to hand over yet.
  - Qt's 'QList<quint32> QSGCurveFillNode::uncookedIndexes() const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSGCurveFillNode is created at the first use, not by
    'QSGCurveFillNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGCurveFillNode.
  - Qt tells when it has removed the C++ QSGCurveFillNode. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGCurveFillNode that has no cute function yet,
    'uncookedIndexes', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QSGCurveFillNode::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurvefillnode.html#tr

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
    #  QString QSGCurveFillNode::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QSGCurveFillNode2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def attributes() -> QSGGeometry.AttributeSet:
    """
    Calls Qt's 'const QSGGeometry::AttributeSet
    &QSGCurveFillNode::attributes()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurvefillnode.html#attributes

    Returns
    -------

    QSGGeometry.AttributeSet
      A new cute QSGGeometry::AttributeSet around the copy Qt gave back.
      Python owns it.
    """
    #  const QSGGeometry::AttributeSet &QSGCurveFillNode::attributes()
    address = Rituals.call('ritual_ZN16QSGCurveFillNode10attributesEv')
    return QSGGeometry.AttributeSet._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGCurveFillNode'

  #  Qt's QSGCurveFillNode is built on more than one class. The part of a C++
  #  QSGCurveFillNode that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QSGCurveAbstractNode':
          'ritual_cast_QSGCurveFillNode_QSGCurveAbstractNode',
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
    Calls Qt's 'const QMetaObject *QSGCurveFillNode::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurvefillnode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGCurveFillNode::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QSGCurveFillNode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QSGCurveFillNode::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurvefillnode.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGCurveFillNode::color() const
    address = self.uglySide.call('ritual_ZNK16QSGCurveFillNode5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def fillTextureProvider(self) -> Optional[QSGTextureProvider]:
    """
    Calls Qt's 'QSGTextureProvider *QSGCurveFillNode::fillTextureProvider()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillnode.html#fillTextureProvider

    Returns
    -------

    Optional[QSGTextureProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTextureProvider *QSGCurveFillNode::fillTextureProvider() const
    address = self.uglySide.call(
        'ritual_ZNK16QSGCurveFillNode19fillTextureProviderEv',
    )
    from . import QSGTextureProvider
    return QSGTextureProvider._cuteAt(address)

  def fillGradient(self) -> Optional[QSGGradientCache.GradientDesc]:
    """
    Calls Qt's 'const QSGGradientCache::GradientDesc
    *QSGCurveFillNode::fillGradient() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurvefillnode.html#fillGradient

    Returns
    -------

    Optional[QSGGradientCache.GradientDesc]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSGGradientCache::GradientDesc *QSGCurveFillNode::fillGradient()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QSGCurveFillNode12fillGradientEv',
    )
    return QSGGradientCache.GradientDesc._cuteAt(address)

  def gradientType(self) -> QGradient.Type:
    """
    Calls Qt's 'QGradient::Type QSGCurveFillNode::gradientType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurvefillnode.html#gradientType

    Returns
    -------

    QGradient.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QGradient.Type(number)'
      gives.
    """
    #  QGradient::Type QSGCurveFillNode::gradientType() const
    return QGradient.Type(self.uglySide.call(
        'ritual_ZNK16QSGCurveFillNode12gradientTypeEv',
    ))

  def fillTransform(self) -> Optional[QSGTransform]:
    """
    Calls Qt's 'const QSGTransform *QSGCurveFillNode::fillTransform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillnode.html#fillTransform

    Returns
    -------

    Optional[QSGTransform]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSGTransform *QSGCurveFillNode::fillTransform() const
    address = self.uglySide.call(
        'ritual_ZNK16QSGCurveFillNode13fillTransformEv',
    )
    from . import QSGTransform
    return QSGTransform._cuteAt(address)

  def debug(self) -> float:
    """
    Calls Qt's 'float QSGCurveFillNode::debug() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurvefillnode.html#debug
    """
    #  float QSGCurveFillNode::debug() const
    return self.uglySide.call('ritual_ZNK16QSGCurveFillNode5debugEv')

  def boundsSize(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QSGCurveFillNode::boundsSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurvefillnode.html#boundsSize

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QSGCurveFillNode::boundsSize() const
    address = self.uglySide.call(
        'ritual_ZNK16QSGCurveFillNode10boundsSizeEv',
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def useStandardDerivatives(self) -> bool:
    """
    Calls Qt's 'bool QSGCurveFillNode::useStandardDerivatives() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillnode.html#useStandardDerivatives
    """
    #  bool QSGCurveFillNode::useStandardDerivatives() const
    return self.uglySide.call(
        'ritual_ZNK16QSGCurveFillNode22useStandardDerivativesEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, col: QColor) -> None:
    """
    Calls Qt's 'void QSGCurveFillNode::setColor(QColor col)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurvefillnode.html#setColor

    Parameters
    ----------

    col : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGCurveFillNode::setColor(QColor col)
    ritual = 'ritual_ZN16QSGCurveFillNode8setColorE6QColor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGCurveFillNode8setColorE6QColor'
    self.uglySide.call(ritual, self._valueOf(col))

  @overload(QSGTextureProvider)
  @overload(NoneType)
  def setFillTextureProvider(
      self,
      provider: Optional[QSGTextureProvider],
  ) -> None:
    """
    Calls Qt's 'void
    QSGCurveFillNode::setFillTextureProvider(QSGTextureProvider *provider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillnode.html#setFillTextureProvider

    Parameters
    ----------

    provider : Optional[QSGTextureProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGCurveFillNode::setFillTextureProvider(QSGTextureProvider
    #      *provider)
    self.uglySide.call(
        'ritual_ZN16QSGCurveFillNode22setFillTextureProviderEP18QSGTextureP'
        'rovider',
        self._addressOf(provider),
    )

  @overload(QSGGradientCache.GradientDesc)
  def setFillGradient(
      self,
      fillGradient: QSGGradientCache.GradientDesc,
  ) -> None:
    """
    Calls Qt's 'void QSGCurveFillNode::setFillGradient(const
    QSGGradientCache::GradientDesc &fillGradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillnode.html#setFillGradient

    Parameters
    ----------

    fillGradient : QSGGradientCache.GradientDesc
      Passed on as a value: Qt reads the C++ QSGGradientCache::GradientDesc,
      which stays Python's own.
    """
    #  void QSGCurveFillNode::setFillGradient(const
    #      QSGGradientCache::GradientDesc &fillGradient)
    self.uglySide.call(
        'ritual_ZN16QSGCurveFillNode15setFillGradientERKN16QSGGradientCache'
        '12GradientDescE',
        self._valueOf(fillGradient),
    )

  @overload(QGradient.Type)
  def setGradientType(self, type: QGradient.Type) -> None:
    """
    Calls Qt's 'void QSGCurveFillNode::setGradientType(QGradient::Type
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillnode.html#setGradientType

    Parameters
    ----------

    type : QGradient.Type
      Passed on as its number.
    """
    #  void QSGCurveFillNode::setGradientType(QGradient::Type type)
    self.uglySide.call(
        'ritual_ZN16QSGCurveFillNode15setGradientTypeEN9QGradient4TypeE',
        type.value,
    )

  @overload(QSGTransform)
  def setFillTransform(self, transform: QSGTransform) -> None:
    """
    Calls Qt's 'void QSGCurveFillNode::setFillTransform(const QSGTransform
    &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillnode.html#setFillTransform

    Parameters
    ----------

    transform : QSGTransform
      Passed on as a value: Qt reads the C++ QSGTransform, which stays
      Python's own.
    """
    #  void QSGCurveFillNode::setFillTransform(const QSGTransform &transform)
    self.uglySide.call(
        'ritual_ZN16QSGCurveFillNode16setFillTransformERK12QSGTransform',
        self._valueOf(transform),
    )

  @overload(float)
  def setDebug(self, newDebug: float) -> None:
    """
    Calls Qt's 'void QSGCurveFillNode::setDebug(float newDebug)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurvefillnode.html#setDebug

    Parameters
    ----------

    newDebug : float
      Passed on as it is.
    """
    #  void QSGCurveFillNode::setDebug(float newDebug)
    self.uglySide.call('ritual_ZN16QSGCurveFillNode8setDebugEf', newDebug)

  @overload(QVector2D)
  def setBoundsSize(self, boundsSize: QVector2D) -> None:
    """
    Calls Qt's 'void QSGCurveFillNode::setBoundsSize(const QVector2D
    &boundsSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillnode.html#setBoundsSize

    Parameters
    ----------

    boundsSize : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QSGCurveFillNode::setBoundsSize(const QVector2D &boundsSize)
    self.uglySide.call(
        'ritual_ZN16QSGCurveFillNode13setBoundsSizeERK9QVector2D',
        self._valueOf(boundsSize),
    )

  @overload(bool)
  def setUseStandardDerivatives(self, useStandardDerivatives: bool) -> None:
    """
    Calls Qt's 'void QSGCurveFillNode::setUseStandardDerivatives(bool
    useStandardDerivatives)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillnode.html#setUseStandardDerivatives

    Parameters
    ----------

    useStandardDerivatives : bool
      Passed on as it is.
    """
    #  void QSGCurveFillNode::setUseStandardDerivatives(bool
    #      useStandardDerivatives)
    ritual = 'ritual_ZN16QSGCurveFillNode25setUseStandardDerivativesEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGCurveFillNode25setUseStandardDerivativesEb'
    self.uglySide.call(ritual, useStandardDerivatives)

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
    Notes what was given, for Qt's 'QSGCurveFillNode::QSGCurveFillNode()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillnode.html#QSGCurveFillNode
    """
    #  QSGCurveFillNode::QSGCurveFillNode()
    self._noteCreation(QSGCurveFillNode, lambda: Rituals.call(
        'ritual_ZN16QSGCurveFillNodeC1Ev',
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

  @overload(
      QVector2D, QVector2D, QVector2D, QVector3D, QVector3D, QVector3D,
      QVector2D, QVector2D, QVector2D, QVector2D, QVector2D,
  )
  def appendTriangle(
      self,
      v1: QVector2D,
      v2: QVector2D,
      v3: QVector2D,
      uv1: QVector3D,
      uv2: QVector3D,
      uv3: QVector3D,
      n1: QVector2D,
      n2: QVector2D,
      n3: QVector2D,
      duvdx: QVector2D,
      duvdy: QVector2D,
  ) -> None:
    """
    Calls Qt's 'void QSGCurveFillNode::appendTriangle(const QVector2D &v1,
    const QVector2D &v2, const QVector2D &v3, const QVector3D &uv1, const
    QVector3D &uv2, const QVector3D &uv3, const QVector2D &n1, const
    QVector2D &n2, const QVector2D &n3, const QVector2D &duvdx, const
    QVector2D &duvdy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillnode.html#appendTriangle

    Parameters
    ----------

    v1 : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    v2 : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    v3 : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    uv1 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    uv2 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    uv3 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    n1 : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    n2 : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    n3 : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    duvdx : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    duvdy : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QSGCurveFillNode::appendTriangle(const QVector2D &v1, const
    #      QVector2D &v2, const QVector2D &v3, const QVector3D &uv1, const
    #      QVector3D &uv2, const QVector3D &uv3, const QVector2D &n1, const
    #      QVector2D &n2, const QVector2D &n3, const QVector2D &duvdx, const
    #      QVector2D &duvdy)
    self.uglySide.call(
        'ritual_ZN16QSGCurveFillNode14appendTriangleERK9QVector2DS2_S2_RK9Q'
        'Vector3DS5_S5_S2_S2_S2_S2_S2_',
        self._valueOf(v1), self._valueOf(v2), self._valueOf(v3),
        self._valueOf(uv1), self._valueOf(uv2), self._valueOf(uv3),
        self._valueOf(n1), self._valueOf(n2), self._valueOf(n3),
        self._valueOf(duvdx), self._valueOf(duvdy),
    )

  def cookGeometry(self) -> None:
    """
    Calls Qt's 'void QSGCurveFillNode::cookGeometry()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurvefillnode.html#cookGeometry
    """
    #  void QSGCurveFillNode::cookGeometry()
    ritual = 'ritual_ZN16QSGCurveFillNode12cookGeometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGCurveFillNode12cookGeometryEv'
    self.uglySide.call(ritual)

  @overload(int)
  def reserve(self, size: int) -> None:
    """
    Calls Qt's 'void QSGCurveFillNode::reserve(qsizetype size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurvefillnode.html#reserve

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QSGCurveFillNode::reserve(qsizetype size)
    self.uglySide.call('ritual_ZN16QSGCurveFillNode7reserveEx', size)

  def preprocess(self) -> None:
    """
    Calls Qt's 'void QSGCurveFillNode::preprocess()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurvefillnode.html#preprocess
    """
    #  void QSGCurveFillNode::preprocess()
    ritual = 'ritual_ZN16QSGCurveFillNode10preprocessEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGCurveFillNode10preprocessEv'
    self.uglySide.call(ritual)

  def handleTextureChanged(self) -> None:
    """
    Calls Qt's 'void QSGCurveFillNode::handleTextureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillnode.html#handleTextureChanged
    """
    #  void QSGCurveFillNode::handleTextureChanged()
    self.uglySide.call('ritual_ZN16QSGCurveFillNode20handleTextureChangedEv')

  def handleTextureProviderDestroyed(self) -> None:
    """
    Calls Qt's 'void QSGCurveFillNode::handleTextureProviderDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillnode.html
    """
    #  void QSGCurveFillNode::handleTextureProviderDestroyed()
    self.uglySide.call(
        'ritual_ZN16QSGCurveFillNode30handleTextureProviderDestroyedEv',
    )

  def updateMaterial(self) -> None:
    """
    Calls Qt's 'void QSGCurveFillNode::updateMaterial()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurvefillnode.html#updateMaterial
    """
    #  void QSGCurveFillNode::updateMaterial()
    self.uglySide.call('ritual_ZN16QSGCurveFillNode14updateMaterialEv')

  @staticmethod
  def uncookedIndexes(*__, **_) -> Never:
    """
    Qt's 'QList<quint32> QSGCurveFillNode::uncookedIndexes() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSGCurveFillNode.uncookedIndexes' has no cute function yet. Qt's "
        "'QList<quint32> QSGCurveFillNode::uncookedIndexes() const': gives "
        "a type Python has no way to take yet.")
