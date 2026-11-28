"""
QQuick3DTextureDataFrontend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qquick3dtexturedatafrontend_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DTextureDataFrontend to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuick3D import QQuick3DTextureData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DTextureDataFrontend(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DTextureDataFrontend: a plain Python object
  standing in front of one C++ QQuick3DTextureDataFrontend.

  What exists
  -----------

  Every function of Qt's QQuick3DTextureDataFrontend that has a ritual and
  that Python can call so far, 19 names in all: 'metaObject', 'tr', 'format',
  'depth', 'setDepth', 'hasTransparency', 'setHasTransparency',
  'textureData', 'setTextureData', 'width', 'setWidth', 'height',
  'setHeight', 'formatChanged', 'depthChanged', 'hasTransparencyChanged',
  'textureDataChanged', 'widthChanged', 'heightChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DTextureDataFrontend::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuick3DTextureDataFrontend::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuick3DTextureDataFrontend::setFormat(const
    QQuick3DTextureData::Format &newFormat)': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DTextureDataFrontend is created at the first use, not by
    'QQuick3DTextureDataFrontend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DTextureDataFrontend.
  - Qt tells when it has removed the C++ QQuick3DTextureDataFrontend. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuick3DTextureDataFrontend::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html#tr

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
    #  QString QQuick3DTextureDataFrontend::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QQuick3DTextureDataFrontend2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DTextureDataFrontend'

  #  A C++ QQuick3DTextureDataFrontend Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DTextureDataFrontend'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DTextureDataFrontend::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DTextureDataFrontend::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuick3DTextureDataFrontend10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def format(self) -> QQuick3DTextureData.Format:
    """
    Calls Qt's 'QQuick3DTextureData::Format
    QQuick3DTextureDataFrontend::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html#format

    Returns
    -------

    QQuick3DTextureData.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DTextureData.Format(number)' gives.
    """
    #  QQuick3DTextureData::Format QQuick3DTextureDataFrontend::format()
    #      const
    return QQuick3DTextureData.Format(self.uglySide.call(
        'ritual_ZNK27QQuick3DTextureDataFrontend6formatEv',
    ))

  def depth(self) -> int:
    """
    Calls Qt's 'int QQuick3DTextureDataFrontend::depth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html#depth
    """
    #  int QQuick3DTextureDataFrontend::depth() const
    return self.uglySide.call(
        'ritual_ZNK27QQuick3DTextureDataFrontend5depthEv',
    )

  def hasTransparency(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DTextureDataFrontend::hasTransparency() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html#hasTransparency
    """
    #  bool QQuick3DTextureDataFrontend::hasTransparency() const
    return self.uglySide.call(
        'ritual_ZNK27QQuick3DTextureDataFrontend15hasTransparencyEv',
    )

  def textureData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQuick3DTextureDataFrontend::textureData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html#textureData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQuick3DTextureDataFrontend::textureData() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuick3DTextureDataFrontend11textureDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def width(self) -> int:
    """
    Calls Qt's 'int QQuick3DTextureDataFrontend::width() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html#width
    """
    #  int QQuick3DTextureDataFrontend::width() const
    return self.uglySide.call(
        'ritual_ZNK27QQuick3DTextureDataFrontend5widthEv',
    )

  def height(self) -> int:
    """
    Calls Qt's 'int QQuick3DTextureDataFrontend::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html#height
    """
    #  int QQuick3DTextureDataFrontend::height() const
    return self.uglySide.call(
        'ritual_ZNK27QQuick3DTextureDataFrontend6heightEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDepth(self, newDepth: int) -> None:
    """
    Calls Qt's 'void QQuick3DTextureDataFrontend::setDepth(int newDepth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html#setDepth

    Parameters
    ----------

    newDepth : int
      Passed on as it is.
    """
    #  void QQuick3DTextureDataFrontend::setDepth(int newDepth)
    self.uglySide.call(
        'ritual_ZN27QQuick3DTextureDataFrontend8setDepthEi', newDepth,
    )

  @overload(bool)
  def setHasTransparency(self, newHasTransparency: bool) -> None:
    """
    Calls Qt's 'void QQuick3DTextureDataFrontend::setHasTransparency(bool
    newHasTransparency)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html

    Parameters
    ----------

    newHasTransparency : bool
      Passed on as it is.
    """
    #  void QQuick3DTextureDataFrontend::setHasTransparency(bool
    #      newHasTransparency)
    self.uglySide.call(
        'ritual_ZN27QQuick3DTextureDataFrontend18setHasTransparencyEb',
        newHasTransparency,
    )

  @overload(QByteArray)
  def setTextureData(self, newTextureData: QByteArray) -> None:
    """
    Calls Qt's 'void QQuick3DTextureDataFrontend::setTextureData(const
    QByteArray &newTextureData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html#setTextureData

    Parameters
    ----------

    newTextureData : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuick3DTextureDataFrontend::setTextureData(const QByteArray
    #      &newTextureData)
    self.uglySide.call(
        'ritual_ZN27QQuick3DTextureDataFrontend14setTextureDataERK10QByteAr'
        'ray',
        self._valueOf(newTextureData),
    )

  @overload(int)
  def setWidth(self, newWidth: int) -> None:
    """
    Calls Qt's 'void QQuick3DTextureDataFrontend::setWidth(int newWidth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html#setWidth

    Parameters
    ----------

    newWidth : int
      Passed on as it is.
    """
    #  void QQuick3DTextureDataFrontend::setWidth(int newWidth)
    self.uglySide.call(
        'ritual_ZN27QQuick3DTextureDataFrontend8setWidthEi', newWidth,
    )

  @overload(int)
  def setHeight(self, newHeight: int) -> None:
    """
    Calls Qt's 'void QQuick3DTextureDataFrontend::setHeight(int newHeight)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html#setHeight

    Parameters
    ----------

    newHeight : int
      Passed on as it is.
    """
    #  void QQuick3DTextureDataFrontend::setHeight(int newHeight)
    self.uglySide.call(
        'ritual_ZN27QQuick3DTextureDataFrontend9setHeightEi', newHeight,
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
    'QQuick3DTextureDataFrontend::QQuick3DTextureDataFrontend()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html
    """
    #  QQuick3DTextureDataFrontend::QQuick3DTextureDataFrontend()
    self._noteCreation(QQuick3DTextureDataFrontend, lambda: Rituals.call(
        'ritual_ZN27QQuick3DTextureDataFrontendC1Ev',
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

  def formatChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTextureDataFrontend::formatChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html#formatChanged
    """
    #  void QQuick3DTextureDataFrontend::formatChanged()
    self.uglySide.call(
        'ritual_ZN27QQuick3DTextureDataFrontend13formatChangedEv',
    )

  def depthChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTextureDataFrontend::depthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html#depthChanged
    """
    #  void QQuick3DTextureDataFrontend::depthChanged()
    self.uglySide.call(
        'ritual_ZN27QQuick3DTextureDataFrontend12depthChangedEv',
    )

  def hasTransparencyChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTextureDataFrontend::hasTransparencyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html
    """
    #  void QQuick3DTextureDataFrontend::hasTransparencyChanged()
    self.uglySide.call(
        'ritual_ZN27QQuick3DTextureDataFrontend22hasTransparencyChangedEv',
    )

  def textureDataChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTextureDataFrontend::textureDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html
    """
    #  void QQuick3DTextureDataFrontend::textureDataChanged()
    self.uglySide.call(
        'ritual_ZN27QQuick3DTextureDataFrontend18textureDataChangedEv',
    )

  def widthChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTextureDataFrontend::widthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html#widthChanged
    """
    #  void QQuick3DTextureDataFrontend::widthChanged()
    self.uglySide.call(
        'ritual_ZN27QQuick3DTextureDataFrontend12widthChangedEv',
    )

  def heightChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DTextureDataFrontend::heightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dtexturedatafrontend.html#heightChanged
    """
    #  void QQuick3DTextureDataFrontend::heightChanged()
    self.uglySide.call(
        'ritual_ZN27QQuick3DTextureDataFrontend13heightChangedEv',
    )
