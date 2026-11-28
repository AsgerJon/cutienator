"""
QSGContextPlugin binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgcontextplugin_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGContextPlugin to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import QSGContextFactoryInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QImage
  from . import QQuickTextureFactory, QSGRenderLoop
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGContextPlugin(QObject, QSGContextFactoryInterface):
  """
  The cute side of Qt's QSGContextPlugin: a plain Python object standing in
  front of one C++ QSGContextPlugin.

  It is built on the cute 'QObject', as Qt's QSGContextPlugin is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QSGContextFactoryInterface' as well, as Qt's QSGContextPlugin is built on
  Qt's QSGContextFactoryInterface too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGContextPlugin that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'tr', 'keys',
  'createTextureFactoryFromImage', 'createWindowManager'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGContextPlugin::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QSGContextPlugin::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QSGContextPlugin::~QSGContextPlugin()': the destructor: Python
    never removes a C++ QSGContextPlugin.

  What has no ritual
  ------------------

  3 of the 11 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QSGContextPlugin is created at the first use, not by
    'QSGContextPlugin(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGContextPlugin.
  - Qt tells when it has removed the C++ QSGContextPlugin. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGContextPlugin that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QSGContextPlugin::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcontextplugin.html#tr

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
    #  QString QSGContextPlugin::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QSGContextPlugin2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGContextPlugin'

  #  Qt's QSGContextPlugin is built on more than one class. The part of a C++
  #  QSGContextPlugin that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QSGContextFactoryInterface':
          'ritual_cast_QSGContextPlugin_QSGContextFactoryInterface',
  }

  #  A C++ QSGContextPlugin Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGContextPlugin'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSGContextPlugin::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcontextplugin.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGContextPlugin::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QSGContextPlugin10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def keys(self) -> QStringList:
    """
    Calls Qt's 'QStringList QSGContextPlugin::keys() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcontextplugin.html#keys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSGContextPlugin::keys() const
    address = self.uglySide.call('ritual_ZNK16QSGContextPlugin4keysEv')
    return QStringList._cuteOwning(address)

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
    Qt's 'QSGContextPlugin::QSGContextPlugin(QObject *parent)': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'QSGContextPlugin.__init__' has no cute function yet. Qt's "
        "'QSGContextPlugin::QSGContextPlugin(QObject *parent)': the class "
        "is abstract, so C++ cannot make one, and the C++ class of ours "
        "does not fill in every function it leaves open.")

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

  @overload(QImage)
  def createTextureFactoryFromImage(
      self,
      a0: QImage,
  ) -> Optional[QQuickTextureFactory]:
    """
    Calls Qt's 'QQuickTextureFactory
    *QSGContextPlugin::createTextureFactoryFromImage(const QImage &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontextplugin.html

    Parameters
    ----------

    a0 : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    Returns
    -------

    Optional[QQuickTextureFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextureFactory
    #      *QSGContextPlugin::createTextureFactoryFromImage(const QImage &a0)
    ritual = (
        'ritual_ZN16QSGContextPlugin29createTextureFactoryFromImageERK6QIma'
        'ge')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QSGContextPlugin29createTextureFactoryFromImageER'
          'K6QImage')
    address = self.uglySide.call(ritual, self._valueOf(a0))
    from . import QQuickTextureFactory
    return QQuickTextureFactory._cuteAt(address)

  def createWindowManager(self) -> Optional[QSGRenderLoop]:
    """
    Calls Qt's 'QSGRenderLoop *QSGContextPlugin::createWindowManager()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontextplugin.html#createWindowManager

    Returns
    -------

    Optional[QSGRenderLoop]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRenderLoop *QSGContextPlugin::createWindowManager()
    ritual = 'ritual_ZN16QSGContextPlugin19createWindowManagerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGContextPlugin19createWindowManagerEv'
    address = self.uglySide.call(ritual)
    from . import QSGRenderLoop
    return QSGRenderLoop._cuteAt(address)
