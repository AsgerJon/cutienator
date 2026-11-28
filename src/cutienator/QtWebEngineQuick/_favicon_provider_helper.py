"""
FaviconProviderHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginefaviconprovider_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means FaviconProviderHelper to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FaviconProviderHelper(QObject):
  """
  The cute side of Qt's FaviconProviderHelper: a plain Python object standing
  in front of one C++ FaviconProviderHelper.

  It is built on the cute 'QObject', as Qt's FaviconProviderHelper is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's FaviconProviderHelper that has a ritual and that
  Python can call so far, 3 names in all: 'metaObject', 'tr', 'instance'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *FaviconProviderHelper::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int FaviconProviderHelper::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void FaviconProviderHelper::attach(QPointer<QQuickWebEngineView>
    view)': takes a type Python has no way to hand over yet.
  - Qt's 'void FaviconProviderHelper::detach(QPointer<QQuickWebEngineView>
    view)': takes a type Python has no way to hand over yet.
  - Qt's 'const QList<QPointer<QQuickWebEngineView>>
    &FaviconProviderHelper::views() const': gives a type Python has no way to
    take yet.
  - Qt's 'void
    FaviconProviderHelper::handleImageRequest(QPointer<FaviconImageResponse>
    faviconResponse)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    FaviconProviderHelper::startFaviconRequest(QPointer<FaviconImageResponse>
    faviconResponse)': takes a type Python has no way to hand over yet.
  - Qt's 'QPointer<QQuickWebEngineView>
    FaviconProviderHelper::findViewByImageSource(const QUrl &imageSource,
    bool isIconUrl) const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ FaviconProviderHelper is created at the first use, not by
    'FaviconProviderHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ FaviconProviderHelper.
  - Qt tells when it has removed the C++ FaviconProviderHelper. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's FaviconProviderHelper that has no cute function yet,
    'attach', 'detach', 'findViewByImageSource', 'handleImageRequest',
    'startFaviconRequest', 'views', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString FaviconProviderHelper::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/faviconproviderhelper.html#tr

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
    #  QString FaviconProviderHelper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21FaviconProviderHelper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def instance() -> Optional[FaviconProviderHelper]:
    """
    Calls Qt's 'FaviconProviderHelper *FaviconProviderHelper::instance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/faviconproviderhelper.html#instance

    Returns
    -------

    Optional[FaviconProviderHelper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FaviconProviderHelper *FaviconProviderHelper::instance()
    address = Rituals.call('ritual_ZN21FaviconProviderHelper8instanceEv')
    return FaviconProviderHelper._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'FaviconProviderHelper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *FaviconProviderHelper::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/faviconproviderhelper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *FaviconProviderHelper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21FaviconProviderHelper10metaObjectEv',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'FaviconProviderHelper::FaviconProviderHelper()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/faviconproviderhelper.html#FaviconProviderHelper
    """
    #  FaviconProviderHelper::FaviconProviderHelper()
    self._noteCreation(FaviconProviderHelper, lambda: Rituals.call(
        'ritual_ZN21FaviconProviderHelperC1Ev',
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

  @staticmethod
  def attach(*__, **_) -> Never:
    """
    Qt's 'void FaviconProviderHelper::attach(QPointer<QQuickWebEngineView>
    view)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'FaviconProviderHelper.attach' has no cute function yet. Qt's "
        "'void FaviconProviderHelper::attach(QPointer<QQuickWebEngineView> "
        "view)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def detach(*__, **_) -> Never:
    """
    Qt's 'void FaviconProviderHelper::detach(QPointer<QQuickWebEngineView>
    view)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'FaviconProviderHelper.detach' has no cute function yet. Qt's "
        "'void FaviconProviderHelper::detach(QPointer<QQuickWebEngineView> "
        "view)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def findViewByImageSource(*__, **_) -> Never:
    """
    Qt's 'QPointer<QQuickWebEngineView>
    FaviconProviderHelper::findViewByImageSource(const QUrl &imageSource,
    bool isIconUrl) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'FaviconProviderHelper.findViewByImageSource' has no cute function "
        "yet. Qt's 'QPointer<QQuickWebEngineView> "
        "FaviconProviderHelper::findViewByImageSource(const QUrl "
        "&imageSource, bool isIconUrl) const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def handleImageRequest(*__, **_) -> Never:
    """
    Qt's 'void
    FaviconProviderHelper::handleImageRequest(QPointer<FaviconImageResponse>
    faviconResponse)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'FaviconProviderHelper.handleImageRequest' has no cute function "
        "yet. Qt's 'void "
        "FaviconProviderHelper::handleImageRequest(QPointer<FaviconImageResp"
        "onse> faviconResponse)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def startFaviconRequest(*__, **_) -> Never:
    """
    Qt's 'void
    FaviconProviderHelper::startFaviconRequest(QPointer<FaviconImageResponse>
    faviconResponse)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'FaviconProviderHelper.startFaviconRequest' has no cute function "
        "yet. Qt's 'void "
        "FaviconProviderHelper::startFaviconRequest(QPointer<FaviconImageRes"
        "ponse> faviconResponse)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def views(*__, **_) -> Never:
    """
    Qt's 'const QList<QPointer<QQuickWebEngineView>>
    &FaviconProviderHelper::views() const': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'FaviconProviderHelper.views' has no cute function yet. Qt's "
        "'const QList<QPointer<QQuickWebEngineView>> "
        "&FaviconProviderHelper::views() const': gives a type Python has no "
        "way to take yet.")
