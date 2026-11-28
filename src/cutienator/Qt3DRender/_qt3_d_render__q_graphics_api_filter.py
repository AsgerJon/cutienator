"""
Qt3DRender::QGraphicsApiFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qgraphicsapifilter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsApiFilter(QObject):
  """
  The cute side of Qt's Qt3DRender::QGraphicsApiFilter: a plain Python object
  standing in front of one C++ Qt3DRender::QGraphicsApiFilter.

  It is built on the cute 'QObject', as Qt's Qt3DRender::QGraphicsApiFilter
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QGraphicsApiFilter that has a ritual and
  that Python can call so far, 22 names in all: 'metaObject', 'tr', 'api',
  'profile', 'minorVersion', 'majorVersion', 'extensions', 'vendor',
  'setApi', 'setProfile', 'setMinorVersion', 'setMajorVersion',
  'setExtensions', 'setVendor', 'apiChanged', 'profileChanged',
  'minorVersionChanged', 'majorVersionChanged', 'extensionsChanged',
  'vendorChanged', 'graphicsApiFilterChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QGraphicsApiFilter::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QGraphicsApiFilter::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QGraphicsApiFilter::~QGraphicsApiFilter()': the
    destructor: Python never removes a C++ Qt3DRender::QGraphicsApiFilter.
  - Qt's 'const QGraphicsApiFilterPrivate
    *Qt3DRender::QGraphicsApiFilter::d_func() const': takes in Python what
    'QGraphicsApiFilterPrivate *Qt3DRender::QGraphicsApiFilter::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QGraphicsApiFilter is created at the first use, not
    by 'Qt3DRender::QGraphicsApiFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QGraphicsApiFilter.
  - Qt tells when it has removed the C++ Qt3DRender::QGraphicsApiFilter.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QGraphicsApiFilter, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class Api(CuteNum):
    """
    The enum 'Qt3DRender::QGraphicsApiFilter::Api' of Qt, with the 5 names Qt
    gives in it.
    """

    OpenGLES = Kee[int](2)
    OpenGL = Kee[int](1)
    Vulkan = Kee[int](3)
    DirectX = Kee[int](4)
    RHI = Kee[int](5)

  class OpenGLProfile(CuteNum):
    """
    The enum 'Qt3DRender::QGraphicsApiFilter::OpenGLProfile' of Qt, with the
    3 names Qt gives in it.
    """

    NoProfile = Kee[int](0)
    CoreProfile = Kee[int](1)
    CompatibilityProfile = Kee[int](2)

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
    Calls Qt's 'QString Qt3DRender::QGraphicsApiFilter::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#tr

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
    #  QString Qt3DRender::QGraphicsApiFilter::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender18QGraphicsApiFilter2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QGraphicsApiFilter'

  #  A C++ Qt3DRender::QGraphicsApiFilter Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QGraphicsApiFilter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DRender::QGraphicsApiFilter::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QGraphicsApiFilter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QGraphicsApiFilter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def api(self) -> Api:
    """
    Calls Qt's 'Api Qt3DRender::QGraphicsApiFilter::api() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#api

    Returns
    -------

    Api
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Api(number)' gives.
    """
    #  Api Qt3DRender::QGraphicsApiFilter::api() const
    return QGraphicsApiFilter.Api(self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QGraphicsApiFilter3apiEv',
    ))

  def profile(self) -> OpenGLProfile:
    """
    Calls Qt's 'OpenGLProfile Qt3DRender::QGraphicsApiFilter::profile()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#profile

    Returns
    -------

    OpenGLProfile
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'OpenGLProfile(number)'
      gives.
    """
    #  OpenGLProfile Qt3DRender::QGraphicsApiFilter::profile() const
    return QGraphicsApiFilter.OpenGLProfile(self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QGraphicsApiFilter7profileEv',
    ))

  def minorVersion(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QGraphicsApiFilter::minorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#minorVersion
    """
    #  int Qt3DRender::QGraphicsApiFilter::minorVersion() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QGraphicsApiFilter12minorVersionEv',
    )

  def majorVersion(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QGraphicsApiFilter::majorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#majorVersion
    """
    #  int Qt3DRender::QGraphicsApiFilter::majorVersion() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QGraphicsApiFilter12majorVersionEv',
    )

  def extensions(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DRender::QGraphicsApiFilter::extensions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#extensions

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DRender::QGraphicsApiFilter::extensions() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QGraphicsApiFilter10extensionsEv',
    )
    return QStringList._cuteOwning(address)

  def vendor(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::QGraphicsApiFilter::vendor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#vendor

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::QGraphicsApiFilter::vendor() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QGraphicsApiFilter6vendorEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Api)
  def setApi(self, api: Api) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGraphicsApiFilter::setApi(Api api)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#setApi

    Parameters
    ----------

    api : Api
      Passed on as its number.
    """
    #  void Qt3DRender::QGraphicsApiFilter::setApi(Api api)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QGraphicsApiFilter6setApiENS0_3ApiE',
        api.value,
    )

  @overload(OpenGLProfile)
  def setProfile(self, profile: OpenGLProfile) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGraphicsApiFilter::setProfile(OpenGLProfile
    profile)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#setProfile

    Parameters
    ----------

    profile : OpenGLProfile
      Passed on as its number.
    """
    #  void Qt3DRender::QGraphicsApiFilter::setProfile(OpenGLProfile profile)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QGraphicsApiFilter10setProfileENS0_13OpenGL'
        'ProfileE',
        profile.value,
    )

  @overload(int)
  def setMinorVersion(self, minorVersion: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGraphicsApiFilter::setMinorVersion(int
    minorVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#setMinorVersion

    Parameters
    ----------

    minorVersion : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGraphicsApiFilter::setMinorVersion(int minorVersion)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QGraphicsApiFilter15setMinorVersionEi',
        minorVersion,
    )

  @overload(int)
  def setMajorVersion(self, majorVersion: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGraphicsApiFilter::setMajorVersion(int
    majorVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#setMajorVersion

    Parameters
    ----------

    majorVersion : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGraphicsApiFilter::setMajorVersion(int majorVersion)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QGraphicsApiFilter15setMajorVersionEi',
        majorVersion,
    )

  @overload(QStringList)
  def setExtensions(self, extensions: QStringList) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGraphicsApiFilter::setExtensions(const
    QStringList &extensions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#setExtensions

    Parameters
    ----------

    extensions : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Qt3DRender::QGraphicsApiFilter::setExtensions(const QStringList
    #      &extensions)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QGraphicsApiFilter13setExtensionsERK5QListI'
        '7QStringE',
        self._valueOf(extensions),
    )

  @overload(str)
  def setVendor(self, vendor: str) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGraphicsApiFilter::setVendor(const QString
    &vendor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#setVendor

    Parameters
    ----------

    vendor : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::QGraphicsApiFilter::setVendor(const QString &vendor)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QGraphicsApiFilter9setVendorERK7QString',
        vendor,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QGraphicsApiFilter::QGraphicsApiFilter(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QGraphicsApiFilter::QGraphicsApiFilter(QObject *parent)
    self._noteCreation(QGraphicsApiFilter, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender18QGraphicsApiFilterC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(Api)
  def apiChanged(self, api: Api) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGraphicsApiFilter::apiChanged(Qt3DRender::
    QGraphicsApiFilter::Api api)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#apiChanged

    Parameters
    ----------

    api : Api
      Passed on as its number.
    """
    #  void Qt3DRender::QGraphicsApiFilter::apiChanged(Qt3DRender::
    #      QGraphicsApiFilter::Api api)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QGraphicsApiFilter10apiChangedENS0_3ApiE',
        api.value,
    )

  @overload(OpenGLProfile)
  def profileChanged(self, profile: OpenGLProfile) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QGraphicsApiFilter::profileChanged(Qt3DRender::
    QGraphicsApiFilter::OpenGLProfile profile)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#profileChanged

    Parameters
    ----------

    profile : OpenGLProfile
      Passed on as its number.
    """
    #  void Qt3DRender::QGraphicsApiFilter::profileChanged(Qt3DRender::
    #      QGraphicsApiFilter::OpenGLProfile profile)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QGraphicsApiFilter14profileChangedENS0_13Op'
        'enGLProfileE',
        profile.value,
    )

  @overload(int)
  def minorVersionChanged(self, minorVersion: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGraphicsApiFilter::minorVersionChanged(int
    minorVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html

    Parameters
    ----------

    minorVersion : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGraphicsApiFilter::minorVersionChanged(int
    #      minorVersion)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QGraphicsApiFilter19minorVersionChangedEi',
        minorVersion,
    )

  @overload(int)
  def majorVersionChanged(self, majorVersion: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGraphicsApiFilter::majorVersionChanged(int
    majorVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html

    Parameters
    ----------

    majorVersion : int
      Passed on as it is.
    """
    #  void Qt3DRender::QGraphicsApiFilter::majorVersionChanged(int
    #      majorVersion)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QGraphicsApiFilter19majorVersionChangedEi',
        majorVersion,
    )

  @overload(QStringList)
  def extensionsChanged(self, extensions: QStringList) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGraphicsApiFilter::extensionsChanged(const
    QStringList &extensions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html

    Parameters
    ----------

    extensions : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Qt3DRender::QGraphicsApiFilter::extensionsChanged(const
    #      QStringList &extensions)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QGraphicsApiFilter17extensionsChangedERK5QL'
        'istI7QStringE',
        self._valueOf(extensions),
    )

  @overload(str)
  def vendorChanged(self, vendor: str) -> None:
    """
    Calls Qt's 'void Qt3DRender::QGraphicsApiFilter::vendorChanged(const
    QString &vendor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#vendorChanged

    Parameters
    ----------

    vendor : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::QGraphicsApiFilter::vendorChanged(const QString
    #      &vendor)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QGraphicsApiFilter13vendorChangedERK7QStrin'
        'g',
        vendor,
    )

  def graphicsApiFilterChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QGraphicsApiFilter::graphicsApiFilterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html
    """
    #  void Qt3DRender::QGraphicsApiFilter::graphicsApiFilterChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QGraphicsApiFilter24graphicsApiFilterChange'
        'dEv',
    )

  def d_func(self) -> Optional[Qt3DRender.QGraphicsApiFilterPrivate]:
    """
    Calls Qt's 'QGraphicsApiFilterPrivate
    *Qt3DRender::QGraphicsApiFilter::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilter.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QGraphicsApiFilterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsApiFilterPrivate *Qt3DRender::QGraphicsApiFilter::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender18QGraphicsApiFilter6d_funcEv',
    )
    return Qt3DRender.QGraphicsApiFilterPrivate._cuteAt(address)
