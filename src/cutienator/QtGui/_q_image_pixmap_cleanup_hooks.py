"""
QImagePixmapCleanupHooks binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qimagepixmapcleanuphooks_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QImagePixmapCleanupHooks to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QImage, QPixmap, QPlatformPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QPixmap = WAIT['QPixmap']
  QPlatformPixmap = WAIT['QPlatformPixmap']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QImagePixmapCleanupHooks(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QImagePixmapCleanupHooks: a plain Python object
  standing in front of one C++ QImagePixmapCleanupHooks.

  C++ hands a QImagePixmapCleanupHooks around as a copy, so every C++
  QImagePixmapCleanupHooks behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QImagePixmapCleanupHooks that has a ritual and that
  Python can call so far, 7 names in all: 'instance', 'enableCleanupHooks',
  'isImageCached', 'isPixmapCached',
  'executePlatformPixmapModificationHooks',
  'executePlatformPixmapDestructionHooks', 'executeImageHooks'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QImagePixmapCleanupHooks::addPlatformPixmapModificationHook(
    _qt_pixmap_cleanup_hook_pmd a0)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QImagePixmapCleanupHooks::addPlatformPixmapDestructionHook(
    _qt_pixmap_cleanup_hook_pmd a0)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void
    QImagePixmapCleanupHooks::addImageHook(_qt_image_cleanup_hook_64 a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void
    QImagePixmapCleanupHooks::removePlatformPixmapModificationHook(
    _qt_pixmap_cleanup_hook_pmd a0)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QImagePixmapCleanupHooks::removePlatformPixmapDestructionHook(
    _qt_pixmap_cleanup_hook_pmd a0)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void
    QImagePixmapCleanupHooks::removeImageHook(_qt_image_cleanup_hook_64 a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QImagePixmapCleanupHooks::~QImagePixmapCleanupHooks()': the
    destructor: Python removes its C++ QImagePixmapCleanupHooks by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QImagePixmapCleanupHooks is created at the first use, not by
    'QImagePixmapCleanupHooks(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QImagePixmapCleanupHooks back gives a copy the ritual
    made for Python, in a new cute QImagePixmapCleanupHooks.
  - Each name of Qt's QImagePixmapCleanupHooks that has no cute function yet,
    'addImageHook', 'addPlatformPixmapDestructionHook',
    'addPlatformPixmapModificationHook', 'removeImageHook',
    'removePlatformPixmapDestructionHook',
    'removePlatformPixmapModificationHook', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def instance() -> Optional[QImagePixmapCleanupHooks]:
    """
    Calls Qt's 'QImagePixmapCleanupHooks
    *QImagePixmapCleanupHooks::instance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagepixmapcleanuphooks.html#instance

    Returns
    -------

    Optional[QImagePixmapCleanupHooks]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QImagePixmapCleanupHooks *QImagePixmapCleanupHooks::instance()
    address = Rituals.call('ritual_ZN24QImagePixmapCleanupHooks8instanceEv')
    return QImagePixmapCleanupHooks._cuteAt(address)

  @staticmethod
  @overload(QImage)
  def enableCleanupHooks(image: QImage) -> None:
    """
    Calls Qt's 'void QImagePixmapCleanupHooks::enableCleanupHooks(const
    QImage &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagepixmapcleanuphooks.html#enableCleanupHooks

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QImagePixmapCleanupHooks::enableCleanupHooks(const QImage &image)
    Rituals.call(
        'ritual_ZN24QImagePixmapCleanupHooks18enableCleanupHooksERK6QImage',
        CuteMixin._valueOf(image),
    )

  @staticmethod
  @overload(QPixmap)
  def enableCleanupHooks(pixmap: QPixmap) -> None:
    """
    Calls Qt's 'void QImagePixmapCleanupHooks::enableCleanupHooks(const
    QPixmap &pixmap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagepixmapcleanuphooks.html#enableCleanupHooks

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QImagePixmapCleanupHooks::enableCleanupHooks(const QPixmap
    #      &pixmap)
    Rituals.call(
        'ritual_ZN24QImagePixmapCleanupHooks18enableCleanupHooksERK7QPixmap',
        CuteMixin._valueOf(pixmap),
    )

  @staticmethod
  @overload(QPlatformPixmap)
  @overload(NoneType)
  def enableCleanupHooks(handle: Optional[QPlatformPixmap]) -> None:
    """
    Calls Qt's 'void
    QImagePixmapCleanupHooks::enableCleanupHooks(QPlatformPixmap *handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagepixmapcleanuphooks.html#enableCleanupHooks

    Parameters
    ----------

    handle : Optional[QPlatformPixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QImagePixmapCleanupHooks::enableCleanupHooks(QPlatformPixmap
    #      *handle)
    Rituals.call(
        'ritual_ZN24QImagePixmapCleanupHooks18enableCleanupHooksEP15QPlatfo'
        'rmPixmap',
        CuteMixin._addressOf(handle),
    )

  @staticmethod
  @overload(QImage)
  def isImageCached(image: QImage) -> bool:
    """
    Calls Qt's 'bool QImagePixmapCleanupHooks::isImageCached(const QImage
    &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagepixmapcleanuphooks.html#isImageCached

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  bool QImagePixmapCleanupHooks::isImageCached(const QImage &image)
    return Rituals.call(
        'ritual_ZN24QImagePixmapCleanupHooks13isImageCachedERK6QImage',
        CuteMixin._valueOf(image),
    )

  @staticmethod
  @overload(QPixmap)
  def isPixmapCached(pixmap: QPixmap) -> bool:
    """
    Calls Qt's 'bool QImagePixmapCleanupHooks::isPixmapCached(const QPixmap
    &pixmap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagepixmapcleanuphooks.html#isPixmapCached

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  bool QImagePixmapCleanupHooks::isPixmapCached(const QPixmap &pixmap)
    return Rituals.call(
        'ritual_ZN24QImagePixmapCleanupHooks14isPixmapCachedERK7QPixmap',
        CuteMixin._valueOf(pixmap),
    )

  @staticmethod
  @overload(QPlatformPixmap)
  @overload(NoneType)
  def executePlatformPixmapModificationHooks(
      a0: Optional[QPlatformPixmap],
  ) -> None:
    """
    Calls Qt's 'void
    QImagePixmapCleanupHooks::executePlatformPixmapModificationHooks(
    QPlatformPixmap *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagepixmapcleanuphooks.html

    Parameters
    ----------

    a0 : Optional[QPlatformPixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QImagePixmapCleanupHooks::executePlatformPixmapModificationHooks(
    #      QPlatformPixmap *a0)
    Rituals.call(
        'ritual_ZN24QImagePixmapCleanupHooks38executePlatformPixmapModifica'
        'tionHooksEP15QPlatformPixmap',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(QPlatformPixmap)
  @overload(NoneType)
  def executePlatformPixmapDestructionHooks(
      a0: Optional[QPlatformPixmap],
  ) -> None:
    """
    Calls Qt's 'void
    QImagePixmapCleanupHooks::executePlatformPixmapDestructionHooks(
    QPlatformPixmap *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagepixmapcleanuphooks.html

    Parameters
    ----------

    a0 : Optional[QPlatformPixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QImagePixmapCleanupHooks::executePlatformPixmapDestructionHooks(
    #      QPlatformPixmap *a0)
    Rituals.call(
        'ritual_ZN24QImagePixmapCleanupHooks37executePlatformPixmapDestruct'
        'ionHooksEP15QPlatformPixmap',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(int)
  def executeImageHooks(key: int) -> None:
    """
    Calls Qt's 'void QImagePixmapCleanupHooks::executeImageHooks(qint64
    key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagepixmapcleanuphooks.html#executeImageHooks

    Parameters
    ----------

    key : int
      Passed on as it is.
    """
    #  void QImagePixmapCleanupHooks::executeImageHooks(qint64 key)
    Rituals.call(
        'ritual_ZN24QImagePixmapCleanupHooks17executeImageHooksEx', key,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QImagePixmapCleanupHooks'

  #  Qt's '~QImagePixmapCleanupHooks()'. Naming it makes this a value class:
  #  Python owns every C++ QImagePixmapCleanupHooks behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QImagePixmapCleanupHooksD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @staticmethod
  def addImageHook(*__, **_) -> Never:
    """
    Qt's 'void
    QImagePixmapCleanupHooks::addImageHook(_qt_image_cleanup_hook_64 a0)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QImagePixmapCleanupHooks.addImageHook' has no cute function yet. "
        "Qt's 'void "
        "QImagePixmapCleanupHooks::addImageHook(_qt_image_cleanup_hook_64 "
        "a0)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def addPlatformPixmapDestructionHook(*__, **_) -> Never:
    """
    Qt's 'void QImagePixmapCleanupHooks::addPlatformPixmapDestructionHook(
    _qt_pixmap_cleanup_hook_pmd a0)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QImagePixmapCleanupHooks.addPlatformPixmapDestructionHook' has no "
        "cute function yet. Qt's 'void "
        "QImagePixmapCleanupHooks::addPlatformPixmapDestructionHook(_qt_pixm"
        "ap_cleanup_hook_pmd a0)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def addPlatformPixmapModificationHook(*__, **_) -> Never:
    """
    Qt's 'void QImagePixmapCleanupHooks::addPlatformPixmapModificationHook(
    _qt_pixmap_cleanup_hook_pmd a0)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QImagePixmapCleanupHooks.addPlatformPixmapModificationHook' has "
        "no cute function yet. Qt's 'void "
        "QImagePixmapCleanupHooks::addPlatformPixmapModificationHook(_qt_pix"
        "map_cleanup_hook_pmd a0)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def removeImageHook(*__, **_) -> Never:
    """
    Qt's 'void
    QImagePixmapCleanupHooks::removeImageHook(_qt_image_cleanup_hook_64 a0)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QImagePixmapCleanupHooks.removeImageHook' has no cute function "
        "yet. Qt's 'void "
        "QImagePixmapCleanupHooks::removeImageHook(_qt_image_cleanup_hook_64"
        " a0)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def removePlatformPixmapDestructionHook(*__, **_) -> Never:
    """
    Qt's 'void QImagePixmapCleanupHooks::removePlatformPixmapDestructionHook(
    _qt_pixmap_cleanup_hook_pmd a0)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QImagePixmapCleanupHooks.removePlatformPixmapDestructionHook' has "
        "no cute function yet. Qt's 'void "
        "QImagePixmapCleanupHooks::removePlatformPixmapDestructionHook(_qt_p"
        "ixmap_cleanup_hook_pmd a0)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def removePlatformPixmapModificationHook(*__, **_) -> Never:
    """
    Qt's 'void
    QImagePixmapCleanupHooks::removePlatformPixmapModificationHook(
    _qt_pixmap_cleanup_hook_pmd a0)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QImagePixmapCleanupHooks.removePlatformPixmapModificationHook' "
        "has no cute function yet. Qt's 'void "
        "QImagePixmapCleanupHooks::removePlatformPixmapModificationHook(_qt_"
        "pixmap_cleanup_hook_pmd a0)': takes a type Python has no way to "
        "hand over yet.")
