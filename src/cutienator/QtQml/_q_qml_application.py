"""
QQmlApplication binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlglobal_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlApplication to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQmlApplicationPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlApplication(QObject):
  """
  The cute side of Qt's QQmlApplication: a plain Python object standing in
  front of one C++ QQmlApplication.

  It is built on the cute 'QObject', as Qt's QQmlApplication is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlApplication that has a ritual and that Python
  can call so far, 17 names in all: 'metaObject', 'tr', 'args', 'name',
  'version', 'organization', 'domain', 'setName', 'setVersion',
  'setOrganization', 'setDomain', 'aboutToQuit', 'nameChanged',
  'versionChanged', 'organizationChanged', 'domainChanged', 'd_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlApplication::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlApplication::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlApplication::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'QQmlApplication::QQmlApplication(QQmlApplicationPrivate &dd,
    QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQmlApplicationPrivate *QQmlApplication::d_func() const':
    takes in Python what 'QQmlApplicationPrivate *QQmlApplication::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlApplication is created at the first use, not by
    'QQmlApplication(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlApplication.
  - Qt tells when it has removed the C++ QQmlApplication. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQmlApplication::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplication.html#tr

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
    #  QString QQmlApplication::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQmlApplication2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlApplication'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlApplication::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplication.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlApplication::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQmlApplication10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QQmlApplication::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplication.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlApplication::name() const
    return self.uglySide.call('ritual_ZNK15QQmlApplication4nameEv')

  def version(self) -> str:
    """
    Calls Qt's 'QString QQmlApplication::version() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplication.html#version

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlApplication::version() const
    return self.uglySide.call('ritual_ZNK15QQmlApplication7versionEv')

  def organization(self) -> str:
    """
    Calls Qt's 'QString QQmlApplication::organization() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplication.html#organization

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlApplication::organization() const
    return self.uglySide.call('ritual_ZNK15QQmlApplication12organizationEv')

  def domain(self) -> str:
    """
    Calls Qt's 'QString QQmlApplication::domain() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplication.html#domain

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlApplication::domain() const
    return self.uglySide.call('ritual_ZNK15QQmlApplication6domainEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, arg: str) -> None:
    """
    Calls Qt's 'void QQmlApplication::setName(const QString &arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplication.html#setName

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlApplication::setName(const QString &arg)
    self.uglySide.call('ritual_ZN15QQmlApplication7setNameERK7QString', arg)

  @overload(str)
  def setVersion(self, arg: str) -> None:
    """
    Calls Qt's 'void QQmlApplication::setVersion(const QString &arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplication.html#setVersion

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlApplication::setVersion(const QString &arg)
    self.uglySide.call(
        'ritual_ZN15QQmlApplication10setVersionERK7QString', arg,
    )

  @overload(str)
  def setOrganization(self, arg: str) -> None:
    """
    Calls Qt's 'void QQmlApplication::setOrganization(const QString &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplication.html#setOrganization

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlApplication::setOrganization(const QString &arg)
    self.uglySide.call(
        'ritual_ZN15QQmlApplication15setOrganizationERK7QString', arg,
    )

  @overload(str)
  def setDomain(self, arg: str) -> None:
    """
    Calls Qt's 'void QQmlApplication::setDomain(const QString &arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplication.html#setDomain

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlApplication::setDomain(const QString &arg)
    self.uglySide.call(
        'ritual_ZN15QQmlApplication9setDomainERK7QString', arg,
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
    Notes what was given, for Qt's 'QQmlApplication::QQmlApplication(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplication.html#QQmlApplication

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlApplication::QQmlApplication(QObject *parent)
    self._noteCreation(QQmlApplication, lambda: Rituals.call(
        'ritual_ZN15QQmlApplicationC1EP7QObject',
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

  def args(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlApplication::args()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplication.html#args

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlApplication::args()
    address = self.uglySide.call('ritual_ZN15QQmlApplication4argsEv')
    return QStringList._cuteOwning(address)

  def aboutToQuit(self) -> None:
    """
    Calls Qt's 'void QQmlApplication::aboutToQuit()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplication.html#aboutToQuit
    """
    #  void QQmlApplication::aboutToQuit()
    self.uglySide.call('ritual_ZN15QQmlApplication11aboutToQuitEv')

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QQmlApplication::nameChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplication.html#nameChanged
    """
    #  void QQmlApplication::nameChanged()
    self.uglySide.call('ritual_ZN15QQmlApplication11nameChangedEv')

  def versionChanged(self) -> None:
    """
    Calls Qt's 'void QQmlApplication::versionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplication.html#versionChanged
    """
    #  void QQmlApplication::versionChanged()
    self.uglySide.call('ritual_ZN15QQmlApplication14versionChangedEv')

  def organizationChanged(self) -> None:
    """
    Calls Qt's 'void QQmlApplication::organizationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplication.html#organizationChanged
    """
    #  void QQmlApplication::organizationChanged()
    self.uglySide.call('ritual_ZN15QQmlApplication19organizationChangedEv')

  def domainChanged(self) -> None:
    """
    Calls Qt's 'void QQmlApplication::domainChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplication.html#domainChanged
    """
    #  void QQmlApplication::domainChanged()
    self.uglySide.call('ritual_ZN15QQmlApplication13domainChangedEv')

  def d_func(self) -> Optional[QQmlApplicationPrivate]:
    """
    Calls Qt's 'QQmlApplicationPrivate *QQmlApplication::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplication.html#d_func

    Returns
    -------

    Optional[QQmlApplicationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlApplicationPrivate *QQmlApplication::d_func()
    address = self.uglySide.call('ritual_ZN15QQmlApplication6d_funcEv')
    from . import QQmlApplicationPrivate
    return QQmlApplicationPrivate._cuteAt(address)
