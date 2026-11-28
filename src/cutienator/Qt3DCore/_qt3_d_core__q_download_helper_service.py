"""
Qt3DCore::QDownloadHelperService binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qdownloadhelperservice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::QDownloadHelperService to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDownloadHelperService(Qt3DCore.QAbstractServiceProvider):
  """
  The cute side of Qt's Qt3DCore::QDownloadHelperService: a plain Python
  object standing in front of one C++ Qt3DCore::QDownloadHelperService.

  It is built on the cute 'Qt3DCore::QAbstractServiceProvider', as Qt's
  Qt3DCore::QDownloadHelperService is built on Qt's
  Qt3DCore::QAbstractServiceProvider, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QDownloadHelperService that has a ritual
  and that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'cancelAllRequests', 'urlToLocalFileOrQrc', 'isLocal', 'getService'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QDownloadHelperService::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int Qt3DCore::QDownloadHelperService::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QDownloadHelperService::~QDownloadHelperService()': the
    destructor: Python never removes a C++ Qt3DCore::QDownloadHelperService.
  - Qt's 'void Qt3DCore::QDownloadHelperService::submitRequest(const
    QDownloadRequestPtr &request)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void Qt3DCore::QDownloadHelperService::cancelRequest(const
    QDownloadRequestPtr &request)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ Qt3DCore::QDownloadHelperService is created at the first use, not
    by 'Qt3DCore::QDownloadHelperService(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QDownloadHelperService.
  - Qt tells when it has removed the C++ Qt3DCore::QDownloadHelperService.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::QDownloadHelperService that has no cute
    function yet, 'cancelRequest', 'submitRequest', holds a function that
    raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString Qt3DCore::QDownloadHelperService::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdownloadhelperservice.html#tr

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
    #  QString Qt3DCore::QDownloadHelperService::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore22QDownloadHelperService2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QUrl)
  def urlToLocalFileOrQrc(url: QUrl) -> str:
    """
    Calls Qt's 'QString
    Qt3DCore::QDownloadHelperService::urlToLocalFileOrQrc(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdownloadhelperservice.html

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QDownloadHelperService::urlToLocalFileOrQrc(const
    #      QUrl &url)
    return Rituals.call(
        'ritual_ZN8Qt3DCore22QDownloadHelperService19urlToLocalFileOrQrcERK'
        '4QUrl',
        CuteMixin._valueOf(url),
    )

  @staticmethod
  @overload(QUrl)
  def isLocal(url: QUrl) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QDownloadHelperService::isLocal(const QUrl
    &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdownloadhelperservice.html#isLocal

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool Qt3DCore::QDownloadHelperService::isLocal(const QUrl &url)
    return Rituals.call(
        'ritual_ZN8Qt3DCore22QDownloadHelperService7isLocalERK4QUrl',
        CuteMixin._valueOf(url),
    )

  @staticmethod
  @overload(WAIT['Qt3DCore.QAspectEngine'])
  @overload(NoneType)
  def getService(
      engine: Optional[Qt3DCore.QAspectEngine],
  ) -> Optional[QDownloadHelperService]:
    """
    Calls Qt's 'QDownloadHelperService
    *Qt3DCore::QDownloadHelperService::getService(QAspectEngine *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdownloadhelperservice.html#getService

    Parameters
    ----------

    engine : Optional[Qt3DCore.QAspectEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDownloadHelperService]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDownloadHelperService
    #      *Qt3DCore::QDownloadHelperService::getService(QAspectEngine
    #      *engine)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore22QDownloadHelperService10getServiceEPNS_13QAspe'
        'ctEngineE',
        CuteMixin._addressOf(engine),
    )
    return QDownloadHelperService._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QDownloadHelperService'

  #  A C++ Qt3DCore::QDownloadHelperService Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QDownloadHelperService'

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
    *Qt3DCore::QDownloadHelperService::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdownloadhelperservice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QDownloadHelperService::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore22QDownloadHelperService10metaObjectEv',
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
  @overload(str)
  def __init__(self, description: str = '') -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QDownloadHelperService::QDownloadHelperService(const QString
    &description)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdownloadhelperservice.html

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  Qt3DCore::QDownloadHelperService::QDownloadHelperService(const QString
    #      &description)
    self._noteCreation(QDownloadHelperService, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore22QDownloadHelperServiceC1ERK7QString',
        description,
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

  def cancelAllRequests(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QDownloadHelperService::cancelAllRequests()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdownloadhelperservice.html
    """
    #  void Qt3DCore::QDownloadHelperService::cancelAllRequests()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore22QDownloadHelperService17cancelAllRequestsEv',
    )

  @staticmethod
  def cancelRequest(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QDownloadHelperService::cancelRequest(const
    QDownloadRequestPtr &request)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QDownloadHelperService.cancelRequest' has no cute "
        "function yet. Qt's 'void "
        "Qt3DCore::QDownloadHelperService::cancelRequest(const "
        "QDownloadRequestPtr &request)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def submitRequest(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QDownloadHelperService::submitRequest(const
    QDownloadRequestPtr &request)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QDownloadHelperService.submitRequest' has no cute "
        "function yet. Qt's 'void "
        "Qt3DCore::QDownloadHelperService::submitRequest(const "
        "QDownloadRequestPtr &request)': takes a type Python has no way to "
        "hand over yet.")
