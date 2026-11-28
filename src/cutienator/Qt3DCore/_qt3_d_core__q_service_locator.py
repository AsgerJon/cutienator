"""
Qt3DCore::QServiceLocator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qservicelocator_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DCore::QServiceLocator to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QServiceLocator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::QServiceLocator: a plain Python object
  standing in front of one C++ Qt3DCore::QServiceLocator.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QServiceLocator that has a ritual and that
  Python can call so far, 9 names in all: 'registerServiceProvider',
  'unregisterServiceProvider', 'serviceCount', 'systemInformation',
  'openGLInformation', 'frameAdvanceService', 'eventFilterService',
  'downloadHelperService', '_q_getServiceHelper'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QServiceLocator::~QServiceLocator()': the destructor:
    Python never removes a C++ Qt3DCore::QServiceLocator.

  What has no ritual
  ------------------

  5 of the 16 functions Qt declares: 2 forbidden; 2 the compiler refuses its
  ritual as it would be written here; 1 a template.

  What to expect
  --------------

  - The C++ Qt3DCore::QServiceLocator is created at the first use, not by
    'Qt3DCore::QServiceLocator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QServiceLocator.
  - Each name of Qt's Qt3DCore::QServiceLocator that has no cute function
    yet, 'd_func', 'service', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DCore::QServiceLocator, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class ServiceType(CuteNum):
    """
    The enum 'Qt3DCore::QServiceLocator::ServiceType' of Qt, with the 8 names
    Qt gives in it.
    """

    SystemInformation = Kee[int](0)
    OpenGLInformation = Kee[int](1)
    CollisionService = Kee[int](2)
    FrameAdvanceService = Kee[int](3)
    EventFilterService = Kee[int](4)
    DownloadHelperService = Kee[int](5)
    DefaultServiceCount = Kee[int](6)
    UserService = Kee[int](256)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QServiceLocator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def serviceCount(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::QServiceLocator::serviceCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qservicelocator.html#serviceCount
    """
    #  int Qt3DCore::QServiceLocator::serviceCount() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore15QServiceLocator12serviceCountEv',
    )

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
  @overload(WAIT['Qt3DCore.QAspectEngine'])
  @overload(NoneType)
  def __init__(
      self,
      aspectEngine: Optional[Qt3DCore.QAspectEngine] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QServiceLocator::QServiceLocator(QAspectEngine
    *aspectEngine)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qservicelocator.html#QServiceLocator

    Parameters
    ----------

    aspectEngine : Optional[Qt3DCore.QAspectEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QServiceLocator::QServiceLocator(QAspectEngine
    #      *aspectEngine)
    self._noteCreation(QServiceLocator, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore15QServiceLocatorC1EPNS_13QAspectEngineE',
        self._addressOf(aspectEngine),
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

  @overload(int, WAIT['Qt3DCore.QAbstractServiceProvider'])
  @overload(int, NoneType)
  def registerServiceProvider(
      self,
      serviceType: int,
      provider: Optional[Qt3DCore.QAbstractServiceProvider],
  ) -> None:
    """
    Calls Qt's 'void Qt3DCore::QServiceLocator::registerServiceProvider(int
    serviceType, QAbstractServiceProvider *provider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qservicelocator.html

    Parameters
    ----------

    serviceType : int
      Passed on as it is.

    provider : Optional[Qt3DCore.QAbstractServiceProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QServiceLocator::registerServiceProvider(int
    #      serviceType, QAbstractServiceProvider *provider)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QServiceLocator23registerServiceProviderEiPNS_'
        '24QAbstractServiceProviderE',
        serviceType, self._addressOf(provider),
    )

  @overload(int)
  def unregisterServiceProvider(self, serviceType: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QServiceLocator::unregisterServiceProvider(int
    serviceType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qservicelocator.html

    Parameters
    ----------

    serviceType : int
      Passed on as it is.
    """
    #  void Qt3DCore::QServiceLocator::unregisterServiceProvider(int
    #      serviceType)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QServiceLocator25unregisterServiceProviderEi',
        serviceType,
    )

  def systemInformation(
      self,
  ) -> Optional[Qt3DCore.QSystemInformationService]:
    """
    Calls Qt's 'QSystemInformationService
    *Qt3DCore::QServiceLocator::systemInformation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qservicelocator.html#systemInformation

    Returns
    -------

    Optional[Qt3DCore.QSystemInformationService]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSystemInformationService
    #      *Qt3DCore::QServiceLocator::systemInformation()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore15QServiceLocator17systemInformationEv',
    )
    return Qt3DCore.QSystemInformationService._cuteAt(address)

  def openGLInformation(
      self,
  ) -> Optional[Qt3DCore.QOpenGLInformationService]:
    """
    Calls Qt's 'QOpenGLInformationService
    *Qt3DCore::QServiceLocator::openGLInformation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qservicelocator.html#openGLInformation

    Returns
    -------

    Optional[Qt3DCore.QOpenGLInformationService]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLInformationService
    #      *Qt3DCore::QServiceLocator::openGLInformation()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore15QServiceLocator17openGLInformationEv',
    )
    return Qt3DCore.QOpenGLInformationService._cuteAt(address)

  def frameAdvanceService(
      self,
  ) -> Optional[Qt3DCore.QAbstractFrameAdvanceService]:
    """
    Calls Qt's 'QAbstractFrameAdvanceService
    *Qt3DCore::QServiceLocator::frameAdvanceService()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qservicelocator.html#frameAdvanceService

    Returns
    -------

    Optional[Qt3DCore.QAbstractFrameAdvanceService]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractFrameAdvanceService
    #      *Qt3DCore::QServiceLocator::frameAdvanceService()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore15QServiceLocator19frameAdvanceServiceEv',
    )
    return Qt3DCore.QAbstractFrameAdvanceService._cuteAt(address)

  def eventFilterService(self) -> Optional[Qt3DCore.QEventFilterService]:
    """
    Calls Qt's 'QEventFilterService
    *Qt3DCore::QServiceLocator::eventFilterService()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qservicelocator.html#eventFilterService

    Returns
    -------

    Optional[Qt3DCore.QEventFilterService]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QEventFilterService *Qt3DCore::QServiceLocator::eventFilterService()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore15QServiceLocator18eventFilterServiceEv',
    )
    return Qt3DCore.QEventFilterService._cuteAt(address)

  def downloadHelperService(
      self,
  ) -> Optional[Qt3DCore.QDownloadHelperService]:
    """
    Calls Qt's 'QDownloadHelperService
    *Qt3DCore::QServiceLocator::downloadHelperService()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qservicelocator.html

    Returns
    -------

    Optional[Qt3DCore.QDownloadHelperService]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDownloadHelperService
    #      *Qt3DCore::QServiceLocator::downloadHelperService()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore15QServiceLocator21downloadHelperServiceEv',
    )
    return Qt3DCore.QDownloadHelperService._cuteAt(address)

  @overload(int)
  def _q_getServiceHelper(
      self,
      type: int,
  ) -> Optional[Qt3DCore.QAbstractServiceProvider]:
    """
    Calls Qt's 'QAbstractServiceProvider
    *Qt3DCore::QServiceLocator::_q_getServiceHelper(int type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qservicelocator.html#_q_getServiceHelper

    Parameters
    ----------

    type : int
      Passed on as it is.

    Returns
    -------

    Optional[Qt3DCore.QAbstractServiceProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractServiceProvider
    #      *Qt3DCore::QServiceLocator::_q_getServiceHelper(int type)
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore15QServiceLocator19_q_getServiceHelperEi', type,
    )
    return Qt3DCore.QAbstractServiceProvider._cuteAt(address)

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QServiceLocatorPrivate *Qt3DCore::QServiceLocator::d_func()': the
      compiler refuses its ritual as it would be written here: unknown type
      name 'QServiceLocatorPrivate'; did you mean
      'Qt3DCore::QServiceLocatorPrivate'?.
    - Qt's 'const QServiceLocatorPrivate *Qt3DCore::QServiceLocator::d_func()
      const': the compiler refuses its ritual as it would be written here:
      unknown type name 'QServiceLocatorPrivate'; did you mean
      'Qt3DCore::QServiceLocatorPrivate'?.
    """
    raise NotImplementedError(
        "'Qt3DCore.QServiceLocator.d_func' has no cute function yet. Qt's "
        "'QServiceLocatorPrivate *Qt3DCore::QServiceLocator::d_func()': the "
        "compiler refuses its ritual as it would be written here: unknown "
        "type name 'QServiceLocatorPrivate'; did you mean "
        "'Qt3DCore::QServiceLocatorPrivate'?. Qt's 'const "
        "QServiceLocatorPrivate *Qt3DCore::QServiceLocator::d_func() "
        "const': the compiler refuses its ritual as it would be written "
        "here: unknown type name 'QServiceLocatorPrivate'; did you mean "
        "'Qt3DCore::QServiceLocatorPrivate'?.")

  @staticmethod
  def service(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QServiceLocator::service': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'Qt3DCore.QServiceLocator.service' has no cute function yet. Qt's "
        "'Qt3DCore::QServiceLocator::service': a template: a pattern and no "
        "single function.")
