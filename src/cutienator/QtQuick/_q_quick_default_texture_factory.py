"""
QQuickDefaultTextureFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpixmap_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickDefaultTextureFactory to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQuickTextureFactory

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtGui import QImage
  from . import QQuickWindow, QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWindow = WAIT['QQuickWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDefaultTextureFactory(QQuickTextureFactory):
  """
  The cute side of Qt's QQuickDefaultTextureFactory: a plain Python object
  standing in front of one C++ QQuickDefaultTextureFactory.

  It is built on the cute 'QQuickTextureFactory', as Qt's
  QQuickDefaultTextureFactory is built on Qt's QQuickTextureFactory, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDefaultTextureFactory that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'createTexture',
  'textureSize', 'textureByteCount', 'image'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDefaultTextureFactory::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickDefaultTextureFactory::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 2 not a gap; 1 leans on
  'QQuickDefaultTextureFactory; 1 leans on 'vtable for
  QQuickDefaultTextureFactory', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickDefaultTextureFactory is created at the first use, not by
    'QQuickDefaultTextureFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDefaultTextureFactory.
  - Qt tells when it has removed the C++ QQuickDefaultTextureFactory. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickDefaultTextureFactory that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDefaultTextureFactory'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickDefaultTextureFactory::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdefaulttexturefactory.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDefaultTextureFactory::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickDefaultTextureFactory10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QQuickWindow)
  @overload(NoneType)
  def createTexture(
      self,
      window: Optional[QQuickWindow],
  ) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture
    *QQuickDefaultTextureFactory::createTexture(QQuickWindow *window) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdefaulttexturefactory.html#createTexture

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QQuickDefaultTextureFactory::createTexture(QQuickWindow
    #      *window) const
    ritual = (
        'ritual_ZNK27QQuickDefaultTextureFactory13createTextureEP12QQuickWi'
        'ndow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QQuickDefaultTextureFactory13createTextureEP12QQ'
          'uickWindow')
    address = self.uglySide.call(ritual, self._addressOf(window))
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickDefaultTextureFactory::textureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdefaulttexturefactory.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickDefaultTextureFactory::textureSize() const
    ritual = 'ritual_ZNK27QQuickDefaultTextureFactory11textureSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QQuickDefaultTextureFactory11textureSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def textureByteCount(self) -> int:
    """
    Calls Qt's 'int QQuickDefaultTextureFactory::textureByteCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdefaulttexturefactory.html#textureByteCount
    """
    #  int QQuickDefaultTextureFactory::textureByteCount() const
    ritual = 'ritual_ZNK27QQuickDefaultTextureFactory16textureByteCountEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QQuickDefaultTextureFactory16textureByteCountEv')
    return self.uglySide.call(ritual)

  def image(self) -> QImage:
    """
    Calls Qt's 'QImage QQuickDefaultTextureFactory::image() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdefaulttexturefactory.html#image

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickDefaultTextureFactory::image() const
    ritual = 'ritual_ZNK27QQuickDefaultTextureFactory5imageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QQuickDefaultTextureFactory5imageEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

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
    Qt's 'QQuickDefaultTextureFactory::QQuickDefaultTextureFactory(const
    QImage &i)': leans on 'vtable for QQuickDefaultTextureFactory', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickDefaultTextureFactory.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickDefaultTextureFactory::QQuickDefaultTextureFactory(const "
        "QImage &i)': leans on 'vtable for QQuickDefaultTextureFactory', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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
