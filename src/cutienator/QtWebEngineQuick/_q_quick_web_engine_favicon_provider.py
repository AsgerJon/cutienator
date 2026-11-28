"""
QQuickWebEngineFaviconProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginefaviconprovider_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineFaviconProvider to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickAsyncImageProvider

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QSize, QUrl
  from ..QtQuick import QQuickImageResponse
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineFaviconProvider(QQuickAsyncImageProvider):
  """
  The cute side of Qt's QQuickWebEngineFaviconProvider: a plain Python object
  standing in front of one C++ QQuickWebEngineFaviconProvider.

  It is built on the cute 'QQuickAsyncImageProvider', as Qt's
  QQuickWebEngineFaviconProvider is built on Qt's QQuickAsyncImageProvider,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineFaviconProvider that has a ritual and
  that Python can call so far, 7 names in all: 'metaObject', 'tr',
  'identifier', 'faviconProviderUrlBase', 'faviconProviderUrl', 'isIconUrl',
  'requestImageResponse'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineFaviconProvider::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickWebEngineFaviconProvider::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickWebEngineFaviconProvider::imageResponseRequested(
    QPointer<FaviconImageResponse> faviconResponse)': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWebEngineFaviconProvider is created at the first use, not
    by 'QQuickWebEngineFaviconProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineFaviconProvider.
  - Qt tells when it has removed the C++ QQuickWebEngineFaviconProvider.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickWebEngineFaviconProvider that has no cute
    function yet, 'imageResponseRequested', holds a function that raises
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
    Calls Qt's 'QString QQuickWebEngineFaviconProvider::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefaviconprovider.html#tr

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
    #  QString QQuickWebEngineFaviconProvider::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN30QQuickWebEngineFaviconProvider2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def identifier() -> str:
    """
    Calls Qt's 'QString QQuickWebEngineFaviconProvider::identifier()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefaviconprovider.html#identifier

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineFaviconProvider::identifier()
    return Rituals.call(
        'ritual_ZN30QQuickWebEngineFaviconProvider10identifierEv',
    )

  @staticmethod
  @overload(QUrl, str)
  def faviconProviderUrlBase(a0: QUrl, identifier: str) -> QUrl:
    """
    Calls Qt's 'QUrl
    QQuickWebEngineFaviconProvider::faviconProviderUrlBase(const QUrl &a0,
    const QString &identifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefaviconprovider.html

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    identifier : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickWebEngineFaviconProvider::faviconProviderUrlBase(const QUrl
    #      &a0, const QString &identifier)
    address = Rituals.call(
        'ritual_ZN30QQuickWebEngineFaviconProvider22faviconProviderUrlBaseE'
        'RK4QUrlRK7QString',
        CuteMixin._valueOf(a0), identifier,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @staticmethod
  @overload(QUrl)
  def faviconProviderUrl(a0: QUrl) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickWebEngineFaviconProvider::faviconProviderUrl(const
    QUrl &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefaviconprovider.html

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickWebEngineFaviconProvider::faviconProviderUrl(const QUrl
    #      &a0)
    address = Rituals.call(
        'ritual_ZN30QQuickWebEngineFaviconProvider18faviconProviderUrlERK4Q'
        'Url',
        CuteMixin._valueOf(a0),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineFaviconProvider'

  #  A C++ QQuickWebEngineFaviconProvider Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebEngineFaviconProvider'

  #  The functions Qt calls itself that QQuickWebEngineFaviconProvider is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'isIconUrl': (
          ('_ZNK30QQuickWebEngineFaviconProvider9isIconUrlEv',
           ('bool', 'number', ''),
           ()),
      ),
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
    Calls Qt's 'const QMetaObject
    *QQuickWebEngineFaviconProvider::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefaviconprovider.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWebEngineFaviconProvider::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuickWebEngineFaviconProvider10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isIconUrl(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineFaviconProvider::isIconUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefaviconprovider.html#isIconUrl
    """
    #  bool QQuickWebEngineFaviconProvider::isIconUrl() const
    ritual = 'ritual_ZNK30QQuickWebEngineFaviconProvider9isIconUrlEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK30QQuickWebEngineFaviconProvider9isIconUrlEv'
    return self.uglySide.call(ritual)

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
    'QQuickWebEngineFaviconProvider::QQuickWebEngineFaviconProvider()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefaviconprovider.html
    """
    #  QQuickWebEngineFaviconProvider::QQuickWebEngineFaviconProvider()
    self._noteCreation(QQuickWebEngineFaviconProvider, lambda: Rituals.call(
        'ritual_ZN30QQuickWebEngineFaviconProviderC1Ev',
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

  @overload(str, QSize)
  def requestImageResponse(
      self,
      id: str,
      requestedSize: QSize,
  ) -> Optional[QQuickImageResponse]:
    """
    Calls Qt's 'QQuickImageResponse
    *QQuickWebEngineFaviconProvider::requestImageResponse(const QString &id,
    const QSize &requestedSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefaviconprovider.html

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    requestedSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    Optional[QQuickImageResponse]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickImageResponse
    #      *QQuickWebEngineFaviconProvider::requestImageResponse(const
    #      QString &id, const QSize &requestedSize)
    ritual = (
        'ritual_ZN30QQuickWebEngineFaviconProvider20requestImageResponseERK'
        '7QStringRK5QSize')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickWebEngineFaviconProvider20requestImageRespo'
          'nseERK7QStringRK5QSize')
    address = self.uglySide.call(ritual, id, self._valueOf(requestedSize))
    from ..QtQuick import QQuickImageResponse
    return QQuickImageResponse._cuteAt(address)

  @staticmethod
  def imageResponseRequested(*__, **_) -> Never:
    """
    Qt's 'void QQuickWebEngineFaviconProvider::imageResponseRequested(
    QPointer<FaviconImageResponse> faviconResponse)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickWebEngineFaviconProvider.imageResponseRequested' has no "
        "cute function yet. Qt's 'void "
        "QQuickWebEngineFaviconProvider::imageResponseRequested(QPointer<Fav"
        "iconImageResponse> faviconResponse)': takes a type Python has no "
        "way to hand over yet.")
