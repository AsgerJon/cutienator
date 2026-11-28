"""
QQuickNinePatchImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickninepatchimage_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickNinePatchImage to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQuick import QQuickImage, QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQuick import QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickNinePatchImage(QQuickImage):
  """
  The cute side of Qt's QQuickNinePatchImage: a plain Python object standing
  in front of one C++ QQuickNinePatchImage.

  It is built on the cute 'QQuickImage', as Qt's QQuickNinePatchImage is
  built on Qt's QQuickImage, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickNinePatchImage that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'topPaddingChanged',
  'leftPaddingChanged', 'rightPaddingChanged', 'bottomPaddingChanged',
  'topInsetChanged', 'leftInsetChanged', 'rightInsetChanged',
  'bottomInsetChanged', 'pixmapChange', 'updatePaintNode'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickNinePatchImage::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickNinePatchImage::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickNinePatchImagePrivate *QQuickNinePatchImage::d_func()': gives
    'QQuickNinePatchImagePrivate', which has no cute class yet.
  - Qt's 'const QQuickNinePatchImagePrivate *QQuickNinePatchImage::d_func()
    const': gives 'QQuickNinePatchImagePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  14 of the 29 functions Qt declares: 9 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  2 forbidden; 1 leans on 'QQuickNinePatchImage.

  What to expect
  --------------

  - The C++ QQuickNinePatchImage is created at the first use, not by
    'QQuickNinePatchImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickNinePatchImage.
  - Qt tells when it has removed the C++ QQuickNinePatchImage. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickNinePatchImage that has no cute function yet,
    '__init__', 'bottomInset', 'bottomPadding', 'leftInset', 'leftPadding',
    'rightInset', 'rightPadding', 'topInset', 'topPadding', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickNinePatchImage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickNinePatchImage::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickninepatchimage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickNinePatchImage::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickNinePatchImage10metaObjectEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickNinePatchImage::QQuickNinePatchImage(QQuickItem *parent)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QQuickNinePatchImagePrivate'.
    """
    raise NotImplementedError(
        "'QQuickNinePatchImage.__init__' has no cute function yet. Qt's "
        "'QQuickNinePatchImage::QQuickNinePatchImage(QQuickItem *parent)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QQuickNinePatchImagePrivate'.")

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

  def topPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickNinePatchImage::topPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickninepatchimage.html#topPaddingChanged
    """
    #  void QQuickNinePatchImage::topPaddingChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickNinePatchImage17topPaddingChangedEv',
    )

  def leftPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickNinePatchImage::leftPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickninepatchimage.html#leftPaddingChanged
    """
    #  void QQuickNinePatchImage::leftPaddingChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickNinePatchImage18leftPaddingChangedEv',
    )

  def rightPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickNinePatchImage::rightPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickninepatchimage.html#rightPaddingChanged
    """
    #  void QQuickNinePatchImage::rightPaddingChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickNinePatchImage19rightPaddingChangedEv',
    )

  def bottomPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickNinePatchImage::bottomPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickninepatchimage.html#bottomPaddingChanged
    """
    #  void QQuickNinePatchImage::bottomPaddingChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickNinePatchImage20bottomPaddingChangedEv',
    )

  def topInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickNinePatchImage::topInsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickninepatchimage.html#topInsetChanged
    """
    #  void QQuickNinePatchImage::topInsetChanged()
    self.uglySide.call('ritual_ZN20QQuickNinePatchImage15topInsetChangedEv')

  def leftInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickNinePatchImage::leftInsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickninepatchimage.html#leftInsetChanged
    """
    #  void QQuickNinePatchImage::leftInsetChanged()
    self.uglySide.call('ritual_ZN20QQuickNinePatchImage16leftInsetChangedEv')

  def rightInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickNinePatchImage::rightInsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickninepatchimage.html#rightInsetChanged
    """
    #  void QQuickNinePatchImage::rightInsetChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickNinePatchImage17rightInsetChangedEv',
    )

  def bottomInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickNinePatchImage::bottomInsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickninepatchimage.html#bottomInsetChanged
    """
    #  void QQuickNinePatchImage::bottomInsetChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickNinePatchImage18bottomInsetChangedEv',
    )

  def pixmapChange(self) -> None:
    """
    Calls Qt's 'void QQuickNinePatchImage::pixmapChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickninepatchimage.html#pixmapChange
    """
    #  void QQuickNinePatchImage::pixmapChange()
    self.uglySide.call('ritual_ZN20QQuickNinePatchImage12pixmapChangeEv')

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      oldNode: Optional[QSGNode],
      data: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickNinePatchImage::updatePaintNode(QSGNode
    *oldNode, UpdatePaintNodeData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickninepatchimage.html#updatePaintNode

    Parameters
    ----------

    oldNode : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickNinePatchImage::updatePaintNode(QSGNode *oldNode,
    #      UpdatePaintNodeData *data)
    address = self.uglySide.call(
        'ritual_ZN20QQuickNinePatchImage15updatePaintNodeEP7QSGNodePN10QQui'
        'ckItem19UpdatePaintNodeDataE',
        self._addressOf(oldNode, 'QSGNode'), self._addressOf(data),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  @staticmethod
  def bottomInset(*__, **_) -> Never:
    """
    Qt's 'qreal QQuickNinePatchImage::bottomInset() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'const
    QQuickNinePatchImagePrivate'.
    """
    raise NotImplementedError(
        "'QQuickNinePatchImage.bottomInset' has no cute function yet. Qt's "
        "'qreal QQuickNinePatchImage::bottomInset() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type 'const "
        "QQuickNinePatchImagePrivate'.")

  @staticmethod
  def bottomPadding(*__, **_) -> Never:
    """
    Qt's 'qreal QQuickNinePatchImage::bottomPadding() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'const
    QQuickNinePatchImagePrivate'.
    """
    raise NotImplementedError(
        "'QQuickNinePatchImage.bottomPadding' has no cute function yet. "
        "Qt's 'qreal QQuickNinePatchImage::bottomPadding() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'const QQuickNinePatchImagePrivate'.")

  @staticmethod
  def leftInset(*__, **_) -> Never:
    """
    Qt's 'qreal QQuickNinePatchImage::leftInset() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'const
    QQuickNinePatchImagePrivate'.
    """
    raise NotImplementedError(
        "'QQuickNinePatchImage.leftInset' has no cute function yet. Qt's "
        "'qreal QQuickNinePatchImage::leftInset() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuickNinePatchImagePrivate'.")

  @staticmethod
  def leftPadding(*__, **_) -> Never:
    """
    Qt's 'qreal QQuickNinePatchImage::leftPadding() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'const
    QQuickNinePatchImagePrivate'.
    """
    raise NotImplementedError(
        "'QQuickNinePatchImage.leftPadding' has no cute function yet. Qt's "
        "'qreal QQuickNinePatchImage::leftPadding() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type 'const "
        "QQuickNinePatchImagePrivate'.")

  @staticmethod
  def rightInset(*__, **_) -> Never:
    """
    Qt's 'qreal QQuickNinePatchImage::rightInset() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'const
    QQuickNinePatchImagePrivate'.
    """
    raise NotImplementedError(
        "'QQuickNinePatchImage.rightInset' has no cute function yet. Qt's "
        "'qreal QQuickNinePatchImage::rightInset() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuickNinePatchImagePrivate'.")

  @staticmethod
  def rightPadding(*__, **_) -> Never:
    """
    Qt's 'qreal QQuickNinePatchImage::rightPadding() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'const
    QQuickNinePatchImagePrivate'.
    """
    raise NotImplementedError(
        "'QQuickNinePatchImage.rightPadding' has no cute function yet. Qt's "
        "'qreal QQuickNinePatchImage::rightPadding() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type 'const "
        "QQuickNinePatchImagePrivate'.")

  @staticmethod
  def topInset(*__, **_) -> Never:
    """
    Qt's 'qreal QQuickNinePatchImage::topInset() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'const
    QQuickNinePatchImagePrivate'.
    """
    raise NotImplementedError(
        "'QQuickNinePatchImage.topInset' has no cute function yet. Qt's "
        "'qreal QQuickNinePatchImage::topInset() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuickNinePatchImagePrivate'.")

  @staticmethod
  def topPadding(*__, **_) -> Never:
    """
    Qt's 'qreal QQuickNinePatchImage::topPadding() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'const
    QQuickNinePatchImagePrivate'.
    """
    raise NotImplementedError(
        "'QQuickNinePatchImage.topPadding' has no cute function yet. Qt's "
        "'qreal QQuickNinePatchImage::topPadding() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuickNinePatchImagePrivate'.")
