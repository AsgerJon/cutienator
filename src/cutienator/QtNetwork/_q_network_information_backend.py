"""
QNetworkInformationBackend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkinformation_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNetworkInformationBackend to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QNetworkInformation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkInformationBackend(QObject):
  """
  The cute side of Qt's QNetworkInformationBackend: a plain Python object
  standing in front of one C++ QNetworkInformationBackend.

  It is built on the cute 'QObject', as Qt's QNetworkInformationBackend is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkInformationBackend that has a ritual and
  that Python can call so far, 16 names in all: 'metaObject', 'tr', 'name',
  'featuresSupported', 'reachability', 'behindCaptivePortal',
  'transportMedium', 'isMetered', 'reachabilityChanged',
  'behindCaptivePortalChanged', 'transportMediumChanged', 'isMeteredChanged',
  'setReachability', 'setBehindCaptivePortal', 'setTransportMedium',
  'setMetered'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNetworkInformationBackend::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QNetworkInformationBackend::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QNetworkInformationBackend::~QNetworkInformationBackend()': the
    destructor: Python never removes a C++ QNetworkInformationBackend.

  What has no ritual
  ------------------

  6 of the 26 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QNetworkInformationBackend is created at the first use, not by
    'QNetworkInformationBackend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkInformationBackend.
  - Qt tells when it has removed the C++ QNetworkInformationBackend. Every
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
    Calls Qt's 'QString QNetworkInformationBackend::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkinformationbackend.html#tr

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
    #  QString QNetworkInformationBackend::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QNetworkInformationBackend2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkInformationBackend'

  #  A C++ QNetworkInformationBackend Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkInformationBackend'

  #  The functions Qt calls itself that QNetworkInformationBackend is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'name': (
          ('_ZNK26QNetworkInformationBackend4nameEv',
           ('address', 'text', ''),
           ()),
      ),
      'featuresSupported': (
          ('_ZNK26QNetworkInformationBackend17featuresSupportedEv',
           ('int', 'flags', 'QtNetwork:QNetworkInformation.Feature'),
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
    Calls Qt's 'const QMetaObject *QNetworkInformationBackend::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackend.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNetworkInformationBackend::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QNetworkInformationBackend10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QNetworkInformationBackend::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackend.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkInformationBackend::name() const
    return self.uglySide.call(
        'ritual_ZNK26QNetworkInformationBackend4nameEv',
    )

  def featuresSupported(self) -> QNetworkInformation.Features:
    """
    Calls Qt's 'QNetworkInformation::Features
    QNetworkInformationBackend::featuresSupported() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackend.html#featuresSupported

    Returns
    -------

    QNetworkInformation.Features
      The value standing for the combination Qt gave back.
    """
    #  QNetworkInformation::Features
    #      QNetworkInformationBackend::featuresSupported() const
    return QNetworkInformation.Features(self.uglySide.call(
        'ritual_ZNK26QNetworkInformationBackend17featuresSupportedEv',
    ))

  def reachability(self) -> QNetworkInformation.Reachability:
    """
    Calls Qt's 'Reachability QNetworkInformationBackend::reachability()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackend.html#reachability

    Returns
    -------

    QNetworkInformation.Reachability
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QNetworkInformation.Reachability(number)' gives.
    """
    #  Reachability QNetworkInformationBackend::reachability() const
    return QNetworkInformation.Reachability(self.uglySide.call(
        'ritual_ZNK26QNetworkInformationBackend12reachabilityEv',
    ))

  def behindCaptivePortal(self) -> bool:
    """
    Calls Qt's 'bool QNetworkInformationBackend::behindCaptivePortal()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackend.html
    """
    #  bool QNetworkInformationBackend::behindCaptivePortal() const
    return self.uglySide.call(
        'ritual_ZNK26QNetworkInformationBackend19behindCaptivePortalEv',
    )

  def transportMedium(self) -> QNetworkInformation.TransportMedium:
    """
    Calls Qt's 'TransportMedium QNetworkInformationBackend::transportMedium()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackend.html#transportMedium

    Returns
    -------

    QNetworkInformation.TransportMedium
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QNetworkInformation.TransportMedium(number)' gives.
    """
    #  TransportMedium QNetworkInformationBackend::transportMedium() const
    return QNetworkInformation.TransportMedium(self.uglySide.call(
        'ritual_ZNK26QNetworkInformationBackend15transportMediumEv',
    ))

  def isMetered(self) -> bool:
    """
    Calls Qt's 'bool QNetworkInformationBackend::isMetered() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackend.html#isMetered
    """
    #  bool QNetworkInformationBackend::isMetered() const
    return self.uglySide.call(
        'ritual_ZNK26QNetworkInformationBackend9isMeteredEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QNetworkInformation.Reachability)
  def setReachability(
      self,
      reachability: QNetworkInformation.Reachability,
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkInformationBackend::setReachability(QNetworkInformation::
    Reachability reachability)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackend.html#setReachability

    Parameters
    ----------

    reachability : QNetworkInformation.Reachability
      Passed on as its number.
    """
    #  void QNetworkInformationBackend::setReachability(QNetworkInformation::
    #      Reachability reachability)
    self.uglySide.call(
        'ritual_ZN26QNetworkInformationBackend15setReachabilityEN19QNetwork'
        'Information12ReachabilityE',
        reachability.value,
    )

  @overload(bool)
  def setBehindCaptivePortal(self, behindPortal: bool) -> None:
    """
    Calls Qt's 'void QNetworkInformationBackend::setBehindCaptivePortal(bool
    behindPortal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackend.html

    Parameters
    ----------

    behindPortal : bool
      Passed on as it is.
    """
    #  void QNetworkInformationBackend::setBehindCaptivePortal(bool
    #      behindPortal)
    self.uglySide.call(
        'ritual_ZN26QNetworkInformationBackend22setBehindCaptivePortalEb',
        behindPortal,
    )

  @overload(QNetworkInformation.TransportMedium)
  def setTransportMedium(
      self,
      medium: QNetworkInformation.TransportMedium,
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkInformationBackend::setTransportMedium(TransportMedium medium)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackend.html#setTransportMedium

    Parameters
    ----------

    medium : QNetworkInformation.TransportMedium
      Passed on as its number.
    """
    #  void QNetworkInformationBackend::setTransportMedium(TransportMedium
    #      medium)
    self.uglySide.call(
        'ritual_ZN26QNetworkInformationBackend18setTransportMediumEN19QNetw'
        'orkInformation15TransportMediumE',
        medium.value,
    )

  @overload(bool)
  def setMetered(self, isMetered: bool) -> None:
    """
    Calls Qt's 'void QNetworkInformationBackend::setMetered(bool isMetered)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackend.html#setMetered

    Parameters
    ----------

    isMetered : bool
      Passed on as it is.
    """
    #  void QNetworkInformationBackend::setMetered(bool isMetered)
    self.uglySide.call(
        'ritual_ZN26QNetworkInformationBackend10setMeteredEb', isMetered,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkInformationBackend::QNetworkInformationBackend()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackend.html
    """
    #  QNetworkInformationBackend::QNetworkInformationBackend()
    self._noteCreation(QNetworkInformationBackend, lambda: Rituals.call(
        'ritual_ZN26QNetworkInformationBackendC1Ev',
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

  @overload(QNetworkInformation.Reachability)
  def reachabilityChanged(
      self,
      reachability: QNetworkInformation.Reachability,
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkInformationBackend::reachabilityChanged(QNetworkInformation::
    Reachability reachability)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackend.html

    Parameters
    ----------

    reachability : QNetworkInformation.Reachability
      Passed on as its number.
    """
    #  void QNetworkInformationBackend::reachabilityChanged(
    #      QNetworkInformation::Reachability reachability)
    self.uglySide.call(
        'ritual_ZN26QNetworkInformationBackend19reachabilityChangedEN19QNet'
        'workInformation12ReachabilityE',
        reachability.value,
    )

  @overload(bool)
  def behindCaptivePortalChanged(self, behindPortal: bool) -> None:
    """
    Calls Qt's 'void
    QNetworkInformationBackend::behindCaptivePortalChanged(bool
    behindPortal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackend.html

    Parameters
    ----------

    behindPortal : bool
      Passed on as it is.
    """
    #  void QNetworkInformationBackend::behindCaptivePortalChanged(bool
    #      behindPortal)
    self.uglySide.call(
        'ritual_ZN26QNetworkInformationBackend26behindCaptivePortalChangedE'
        'b',
        behindPortal,
    )

  @overload(QNetworkInformation.TransportMedium)
  def transportMediumChanged(
      self,
      medium: QNetworkInformation.TransportMedium,
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkInformationBackend::transportMediumChanged(QNetworkInformation::
    TransportMedium medium)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackend.html

    Parameters
    ----------

    medium : QNetworkInformation.TransportMedium
      Passed on as its number.
    """
    #  void QNetworkInformationBackend::transportMediumChanged(
    #      QNetworkInformation::TransportMedium medium)
    self.uglySide.call(
        'ritual_ZN26QNetworkInformationBackend22transportMediumChangedEN19Q'
        'NetworkInformation15TransportMediumE',
        medium.value,
    )

  @overload(bool)
  def isMeteredChanged(self, isMetered: bool) -> None:
    """
    Calls Qt's 'void QNetworkInformationBackend::isMeteredChanged(bool
    isMetered)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackend.html#isMeteredChanged

    Parameters
    ----------

    isMetered : bool
      Passed on as it is.
    """
    #  void QNetworkInformationBackend::isMeteredChanged(bool isMetered)
    self.uglySide.call(
        'ritual_ZN26QNetworkInformationBackend16isMeteredChangedEb',
        isMetered,
    )
