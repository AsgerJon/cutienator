"""
Qt3DRender::QTextureLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qtexture.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextureLoader(Qt3DRender.QAbstractTexture):
  """
  The cute side of Qt's Qt3DRender::QTextureLoader: a plain Python object
  standing in front of one C++ Qt3DRender::QTextureLoader.

  It is built on the cute 'Qt3DRender::QAbstractTexture', as Qt's
  Qt3DRender::QTextureLoader is built on Qt's Qt3DRender::QAbstractTexture,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QTextureLoader that has a ritual and
  that Python can call so far, 9 names in all: 'metaObject', 'tr', 'source',
  'isMirrored', 'setSource', 'setMirrored', 'sourceChanged',
  'mirroredChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QTextureLoader::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QTextureLoader::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QTextureLoader::~QTextureLoader()': the destructor:
    Python never removes a C++ Qt3DRender::QTextureLoader.
  - Qt's 'const QTextureLoaderPrivate *Qt3DRender::QTextureLoader::d_func()
    const': takes in Python what 'QTextureLoaderPrivate
    *Qt3DRender::QTextureLoader::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QTextureLoader is created at the first use, not by
    'Qt3DRender::QTextureLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QTextureLoader.
  - Qt tells when it has removed the C++ Qt3DRender::QTextureLoader. Every
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
    Calls Qt's 'QString Qt3DRender::QTextureLoader::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qtextureloader.html#tr

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
    #  QString Qt3DRender::QTextureLoader::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender14QTextureLoader2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QTextureLoader'

  #  A C++ Qt3DRender::QTextureLoader Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QTextureLoader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QTextureLoader::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureloader.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QTextureLoader::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QTextureLoader10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl Qt3DRender::QTextureLoader::source() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureloader.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DRender::QTextureLoader::source() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QTextureLoader6sourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def isMirrored(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QTextureLoader::isMirrored() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureloader.html#isMirrored
    """
    #  bool Qt3DRender::QTextureLoader::isMirrored() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QTextureLoader10isMirroredEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureLoader::setSource(const QUrl
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureloader.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QTextureLoader::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QTextureLoader9setSourceERK4QUrl',
        self._valueOf(source),
    )

  @overload(bool)
  def setMirrored(self, mirrored: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureLoader::setMirrored(bool mirrored)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureloader.html#setMirrored

    Parameters
    ----------

    mirrored : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureLoader::setMirrored(bool mirrored)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QTextureLoader11setMirroredEb', mirrored,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QTextureLoader::QTextureLoader(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureloader.html#QTextureLoader

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QTextureLoader::QTextureLoader(Qt3DCore::QNode *parent)
    self._noteCreation(QTextureLoader, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender14QTextureLoaderC1EPN8Qt3DCore5QNodeE',
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

  @overload(QUrl)
  def sourceChanged(self, source: QUrl) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureLoader::sourceChanged(const QUrl
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureloader.html#sourceChanged

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QTextureLoader::sourceChanged(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QTextureLoader13sourceChangedERK4QUrl',
        self._valueOf(source),
    )

  @overload(bool)
  def mirroredChanged(self, mirrored: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureLoader::mirroredChanged(bool
    mirrored)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureloader.html#mirroredChanged

    Parameters
    ----------

    mirrored : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureLoader::mirroredChanged(bool mirrored)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QTextureLoader15mirroredChangedEb', mirrored,
    )

  def d_func(self) -> Optional[Qt3DRender.QTextureLoaderPrivate]:
    """
    Calls Qt's 'QTextureLoaderPrivate *Qt3DRender::QTextureLoader::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureloader.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QTextureLoaderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextureLoaderPrivate *Qt3DRender::QTextureLoader::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender14QTextureLoader6d_funcEv',
    )
    return Qt3DRender.QTextureLoaderPrivate._cuteAt(address)
