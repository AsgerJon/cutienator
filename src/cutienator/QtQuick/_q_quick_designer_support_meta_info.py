"""
QQuickDesignerSupportMetaInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdesignersupportmetainfo_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickDesignerSupportMetaInfo to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDesignerSupportMetaInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickDesignerSupportMetaInfo: a plain Python object
  standing in front of one C++ QQuickDesignerSupportMetaInfo.

  C++ hands a QQuickDesignerSupportMetaInfo around as a copy, so every C++
  QQuickDesignerSupportMetaInfo behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQuickDesignerSupportMetaInfo that has a ritual and
  that Python can call so far, 2 names in all: 'isSubclassOf',
  'registerMockupObject'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QQuickDesignerSupportMetaInfo::registerNotifyPropertyChangeCallBack(void
    (*)(QObject *, const QQuickDesignerSupport::PropertyName &) callback)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQuickDesignerSupportMetaInfo::~QQuickDesignerSupportMetaInfo()':
    the destructor: Python removes its C++ QQuickDesignerSupportMetaInfo by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQuickDesignerSupportMetaInfo is created at the first use, not by
    'QQuickDesignerSupportMetaInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickDesignerSupportMetaInfo back gives a copy the
    ritual made for Python, in a new cute QQuickDesignerSupportMetaInfo.
  - Each name of Qt's QQuickDesignerSupportMetaInfo that has no cute function
    yet, 'registerNotifyPropertyChangeCallBack', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QObject, QByteArray)
  @overload(NoneType, QByteArray)
  def isSubclassOf(
      object: Optional[QObject],
      superTypeName: QByteArray,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDesignerSupportMetaInfo::isSubclassOf(QObject
    *object, const QByteArray &superTypeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportmetainfo.html#isSubclassOf

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    superTypeName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QQuickDesignerSupportMetaInfo::isSubclassOf(QObject *object,
    #      const QByteArray &superTypeName)
    return Rituals.call(
        'ritual_ZN29QQuickDesignerSupportMetaInfo12isSubclassOfEP7QObjectRK'
        '10QByteArray',
        CuteMixin._addressOf(object, 'QObject'),
        CuteMixin._valueOf(superTypeName),
    )

  @staticmethod
  @overload(str, int, int, str)
  @overload(str, int, int, NoneType)
  @overload(NoneType, int, int, str)
  @overload(NoneType, int, int, NoneType)
  def registerMockupObject(
      uri: Optional[str],
      versionMajor: int,
      versionMinor: int,
      qmlName: Optional[str],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDesignerSupportMetaInfo::registerMockupObject(const char *uri, int
    versionMajor, int versionMinor, const char *qmlName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportmetainfo.html

    Parameters
    ----------

    uri : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    versionMajor : int
      Passed on as it is.

    versionMinor : int
      Passed on as it is.

    qmlName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QQuickDesignerSupportMetaInfo::registerMockupObject(const char
    #      *uri, int versionMajor, int versionMinor, const char *qmlName)
    Rituals.call(
        'ritual_ZN29QQuickDesignerSupportMetaInfo20registerMockupObjectEPKc'
        'iiS1_',
        CuteMixin._bytesOf(uri), versionMajor, versionMinor,
        CuteMixin._bytesOf(qmlName),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDesignerSupportMetaInfo'

  #  Qt's '~QQuickDesignerSupportMetaInfo()'. Naming it makes this a value
  #  class: Python owns every C++ QQuickDesignerSupportMetaInfo behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QQuickDesignerSupportMetaInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def registerNotifyPropertyChangeCallBack(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickDesignerSupportMetaInfo::registerNotifyPropertyChangeCallBack(void
    (*)(QObject *, const QQuickDesignerSupport::PropertyName &) callback)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickDesignerSupportMetaInfo.registerNotifyPropertyChangeCallBack"
        "' has no cute function yet. Qt's 'void "
        "QQuickDesignerSupportMetaInfo::registerNotifyPropertyChangeCallBack"
        "(void (*)(QObject *, const QQuickDesignerSupport::PropertyName &) "
        "callback)': takes a type Python has no way to hand over yet.")
