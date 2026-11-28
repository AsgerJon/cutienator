"""
QQuickPackage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qquickpackage_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickPackage to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickPackageAttached

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPackage(QObject):
  """
  The cute side of Qt's QQuickPackage: a plain Python object standing in
  front of one C++ QQuickPackage.

  It is built on the cute 'QObject', as Qt's QQuickPackage is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPackage that has a ritual and that Python can
  call so far, 5 names in all: 'metaObject', 'tr', 'part', 'hasPart',
  'qmlAttachedProperties'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPackage::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickPackage::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickPackagePrivate *QQuickPackage::d_func()': gives
    'QQuickPackagePrivate', which has no cute class yet.
  - Qt's 'const QQuickPackagePrivate *QQuickPackage::d_func() const': gives
    'QQuickPackagePrivate', which has no cute class yet.
  - Qt's 'void QQuickPackage::qt_qmlMarker_attached()': one of Qt's own inner
    workings.
  - Qt's 'QQmlListProperty<QObject> QQuickPackage::data()': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPackage is created at the first use, not by
    'QQuickPackage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPackage.
  - Qt tells when it has removed the C++ QQuickPackage. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickPackage that has no cute function yet, 'data',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString QQuickPackage::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpackage.html#tr

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
    #  QString QQuickPackage::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQuickPackage2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      a0: Optional[QObject],
  ) -> Optional[QQuickPackageAttached]:
    """
    Calls Qt's 'QQuickPackageAttached
    *QQuickPackage::qmlAttachedProperties(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpackage.html#qmlAttachedProperties

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickPackageAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPackageAttached *QQuickPackage::qmlAttachedProperties(QObject
    #      *a0)
    address = Rituals.call(
        'ritual_ZN13QQuickPackage21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(a0, 'QObject'),
    )
    from . import QQuickPackageAttached
    return QQuickPackageAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPackage'

  #  A C++ QQuickPackage Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPackage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPackage::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpackage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPackage::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQuickPackage10metaObjectEv')
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
    Notes what was given, for Qt's 'QQuickPackage::QQuickPackage(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickpackage.html#QQuickPackage

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPackage::QQuickPackage(QObject *parent)
    self._noteCreation(QQuickPackage, lambda: Rituals.call(
        'ritual_ZN13QQuickPackageC1EP7QObject',
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

  @overload()
  @overload(str)
  def part(self, a0: str = '') -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickPackage::part(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpackage.html#part

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickPackage::part(const QString &a0)
    address = self.uglySide.call(
        'ritual_ZN13QQuickPackage4partERK7QString', a0,
    )
    return QObject._cuteAt(address)

  @overload(str)
  def hasPart(self, a0: str) -> bool:
    """
    Calls Qt's 'bool QQuickPackage::hasPart(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpackage.html#hasPart

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQuickPackage::hasPart(const QString &a0)
    return self.uglySide.call(
        'ritual_ZN13QQuickPackage7hasPartERK7QString', a0,
    )

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickPackage::data()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickPackage.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickPackage::data()': gives a type "
        "Python has no way to take yet.")
