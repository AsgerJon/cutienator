"""
Qt3DRender::QRenderAspect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qrenderaspect.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRenderAspect(Qt3DCore.QAbstractAspect):
  """
  The cute side of Qt's Qt3DRender::QRenderAspect: a plain Python object
  standing in front of one C++ Qt3DRender::QRenderAspect.

  It is built on the cute 'Qt3DCore::QAbstractAspect', as Qt's
  Qt3DRender::QRenderAspect is built on Qt's Qt3DCore::QAbstractAspect, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QRenderAspect that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'd_func',
  'executeCommand', 'onRegistered', 'onUnregistered', 'onEngineStartup',
  'dependencies'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QRenderAspect::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QRenderAspect::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QRenderAspect::~QRenderAspect()': the destructor:
    Python never removes a C++ Qt3DRender::QRenderAspect.
  - Qt's 'Qt3DRender::QRenderAspect::QRenderAspect(QRenderAspectPrivate &dd,
    QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QRenderAspectPrivate *Qt3DRender::QRenderAspect::d_func()
    const': takes in Python what 'QRenderAspectPrivate
    *Qt3DRender::QRenderAspect::d_func()' takes.
  - Qt's 'std::vector<Qt3DCore::QAspectJobPtr>
    Qt3DRender::QRenderAspect::jobsToExecute(qint64 time)': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QRenderAspect is created at the first use, not by
    'Qt3DRender::QRenderAspect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QRenderAspect.
  - Qt tells when it has removed the C++ Qt3DRender::QRenderAspect. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QRenderAspect, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class SubmissionType(CuteNum):
    """
    The enum 'Qt3DRender::QRenderAspect::SubmissionType' of Qt, with the 2
    names Qt gives in it.
    """

    Automatic = Kee[int](0)
    Manual = Kee[int](1)

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
    Calls Qt's 'QString Qt3DRender::QRenderAspect::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qrenderaspect.html#tr

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
    #  QString Qt3DRender::QRenderAspect::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender13QRenderAspect2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QRenderAspect'

  #  A C++ Qt3DRender::QRenderAspect Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QRenderAspect'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QRenderAspect::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspect.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QRenderAspect::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QRenderAspect10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dependencies(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DRender::QRenderAspect::dependencies() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspect.html#dependencies

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DRender::QRenderAspect::dependencies() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QRenderAspect12dependenciesEv',
    )
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QRenderAspect::QRenderAspect(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspect.html#QRenderAspect

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QRenderAspect::QRenderAspect(QObject *parent)
    self._noteCreation(QRenderAspect, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender13QRenderAspectC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(SubmissionType)
  @overload(SubmissionType, QObject)
  @overload(SubmissionType, NoneType)
  def __init__(
      self,
      submissionType: SubmissionType,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QRenderAspect::QRenderAspect(SubmissionType submissionType,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspect.html#QRenderAspect

    Parameters
    ----------

    submissionType : SubmissionType
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QRenderAspect::QRenderAspect(SubmissionType
    #      submissionType, QObject *parent)
    self._noteCreation(QRenderAspect, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender13QRenderAspectC1ENS0_14SubmissionTypeEP7QObj'
        'ect',
        submissionType.value, self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[Qt3DRender.QRenderAspectPrivate]:
    """
    Calls Qt's 'QRenderAspectPrivate *Qt3DRender::QRenderAspect::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspect.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QRenderAspectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderAspectPrivate *Qt3DRender::QRenderAspect::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender13QRenderAspect6d_funcEv',
    )
    return Qt3DRender.QRenderAspectPrivate._cuteAt(address)

  @overload(QStringList)
  def executeCommand(self, args: QStringList) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DRender::QRenderAspect::executeCommand(const
    QStringList &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspect.html#executeCommand

    Parameters
    ----------

    args : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DRender::QRenderAspect::executeCommand(const QStringList
    #      &args)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender13QRenderAspect14executeCommandERK5QListI7QSt'
        'ringE',
        self._valueOf(args),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def onRegistered(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderAspect::onRegistered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspect.html#onRegistered
    """
    #  void Qt3DRender::QRenderAspect::onRegistered()
    ritual = 'ritual_ZN10Qt3DRender13QRenderAspect12onRegisteredEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10Qt3DRender13QRenderAspect12onRegisteredEv'
    self.uglySide.call(ritual)

  def onUnregistered(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderAspect::onUnregistered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspect.html#onUnregistered
    """
    #  void Qt3DRender::QRenderAspect::onUnregistered()
    ritual = 'ritual_ZN10Qt3DRender13QRenderAspect14onUnregisteredEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10Qt3DRender13QRenderAspect14onUnregisteredEv'
    self.uglySide.call(ritual)

  def onEngineStartup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderAspect::onEngineStartup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspect.html#onEngineStartup
    """
    #  void Qt3DRender::QRenderAspect::onEngineStartup()
    ritual = 'ritual_ZN10Qt3DRender13QRenderAspect15onEngineStartupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10Qt3DRender13QRenderAspect15onEngineStartupEv'
    self.uglySide.call(ritual)
