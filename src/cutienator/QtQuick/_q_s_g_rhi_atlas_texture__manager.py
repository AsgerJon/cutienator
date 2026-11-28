"""
QSGRhiAtlasTexture::Manager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGRhiAtlasTexture::Manager to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class Manager(QObject):
  """
  The cute side of Qt's QSGRhiAtlasTexture::Manager: a plain Python object
  standing in front of one C++ QSGRhiAtlasTexture::Manager.

  It is built on the cute 'QObject', as Qt's QSGRhiAtlasTexture::Manager is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGRhiAtlasTexture::Manager that has a ritual and
  that Python can call so far, 2 names in all: 'metaObject', 'invalidate'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGRhiAtlasTexture::Manager::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QSGRhiAtlasTexture::Manager::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QSGRhiAtlasTexture::Manager::~Manager()': the destructor: Python
    never removes a C++ QSGRhiAtlasTexture::Manager.

  What has no ritual
  ------------------

  6 of the 11 functions Qt declares: 2 not a gap; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 2
  leans on 'QSGRhiAtlasTexture.

  What to expect
  --------------

  - The C++ QSGRhiAtlasTexture::Manager is created at the first use, not by
    'QSGRhiAtlasTexture::Manager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGRhiAtlasTexture::Manager.
  - Qt tells when it has removed the C++ QSGRhiAtlasTexture::Manager. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGRhiAtlasTexture::Manager that has no cute function
    yet, '__init__', 'create', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGRhiAtlasTexture::Manager'

  #  A C++ QSGRhiAtlasTexture::Manager Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGRhiAtlasTexture_Manager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSGRhiAtlasTexture::Manager::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-manager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGRhiAtlasTexture::Manager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QSGRhiAtlasTexture7Manager10metaObjectEv',
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
    Qt's 'QSGRhiAtlasTexture::Manager::Manager(QSGDefaultRenderContext *rc,
    const QSize &surfacePixelSize, QSurface *maybeSurface)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'qt_sg_envInt'.
    """
    raise NotImplementedError(
        "'QSGRhiAtlasTexture.Manager.__init__' has no cute function yet. "
        "Qt's 'QSGRhiAtlasTexture::Manager::Manager(QSGDefaultRenderContext "
        "*rc, const QSize &surfacePixelSize, QSurface *maybeSurface)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qt_sg_envInt'.")

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

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QSGRhiAtlasTexture::Manager::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-manager.html#invalidate
    """
    #  void QSGRhiAtlasTexture::Manager::invalidate()
    self.uglySide.call('ritual_ZN18QSGRhiAtlasTexture7Manager10invalidateEv')

  @staticmethod
  def create(*__, **_) -> Never:
    """
    - Qt's 'QSGTexture *QSGRhiAtlasTexture::Manager::create(const
      QSGCompressedTextureFactory *factory)': Qt's library has no name for
      it, and its code in Qt's source does not compile apart from its file:
      use of undeclared identifier 'qsgEnableCompressedAtlas'.
    - Qt's 'QSGTexture *QSGRhiAtlasTexture::Manager::create(const QImage
      &image, bool hasAlphaChannel)': leans on
      'QSGRhiAtlasTexture::Atlas::Atlas(QSGDefaultRenderContext*, QSize
      const&)', which Qt's source does not mark for use from outside Qt and
      has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGRhiAtlasTexture.Manager.create' has no cute function yet. Qt's "
        "'QSGTexture *QSGRhiAtlasTexture::Manager::create(const "
        "QSGCompressedTextureFactory *factory)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'qsgEnableCompressedAtlas'. "
        "Qt's 'QSGTexture *QSGRhiAtlasTexture::Manager::create(const QImage "
        "&image, bool hasAlphaChannel)': leans on "
        "'QSGRhiAtlasTexture::Atlas::Atlas(QSGDefaultRenderContext*, QSize "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
