"""
Qt3DInput::QInputDevicePlugin binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/qinputdeviceplugin_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DInput::QInputDevicePlugin to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QInputDevicePlugin(QObject):
  """
  The cute side of Qt's Qt3DInput::QInputDevicePlugin: a plain Python object
  standing in front of one C++ Qt3DInput::QInputDevicePlugin.

  It is built on the cute 'QObject', as Qt's Qt3DInput::QInputDevicePlugin is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QInputDevicePlugin that has a ritual and
  that Python can call so far, 3 names in all: 'metaObject', 'tr', 'create'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QInputDevicePlugin::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DInput::QInputDevicePlugin::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QInputDevicePlugin::~QInputDevicePlugin()': the
    destructor: Python never removes a C++ Qt3DInput::QInputDevicePlugin.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QInputDevicePlugin is created at the first use, not by
    'Qt3DInput::QInputDevicePlugin(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QInputDevicePlugin.
  - Qt tells when it has removed the C++ Qt3DInput::QInputDevicePlugin. Every
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
    Calls Qt's 'QString Qt3DInput::QInputDevicePlugin::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputdeviceplugin.html#tr

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
    #  QString Qt3DInput::QInputDevicePlugin::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput18QInputDevicePlugin2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QInputDevicePlugin'

  #  A C++ Qt3DInput::QInputDevicePlugin Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QInputDevicePlugin'

  #  The functions Qt calls itself that Qt3DInput::QInputDevicePlugin is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'create': (
          'QInputDeviceIntegration '
          '*Qt3DInput::QInputDevicePlugin::create(const QString &, const '
          'QStringList &)',
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
    *Qt3DInput::QInputDevicePlugin::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputdeviceplugin.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QInputDevicePlugin::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput18QInputDevicePlugin10metaObjectEv',
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DInput::QInputDevicePlugin::QInputDevicePlugin(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputdeviceplugin.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DInput::QInputDevicePlugin::QInputDevicePlugin(QObject *parent)
    self._noteCreation(QInputDevicePlugin, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput18QInputDevicePluginC1EP7QObject',
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

  @overload(str, QStringList)
  def create(
      self,
      key: str,
      paramList: QStringList,
  ) -> Optional[Qt3DInput.QInputDeviceIntegration]:
    """
    Calls Qt's 'QInputDeviceIntegration
    *Qt3DInput::QInputDevicePlugin::create(const QString &key, const
    QStringList &paramList)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputdeviceplugin.html#create

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    paramList : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[Qt3DInput.QInputDeviceIntegration]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputDeviceIntegration *Qt3DInput::QInputDevicePlugin::create(const
    #      QString &key, const QStringList &paramList)
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput18QInputDevicePlugin6createERK7QStringRK5QListI'
        'S1_E',
        key, self._valueOf(paramList),
    )
    return Qt3DInput.QInputDeviceIntegration._cuteAt(address)
