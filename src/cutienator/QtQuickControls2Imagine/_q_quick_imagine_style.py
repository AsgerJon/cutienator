"""
QQuickImagineStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Imagine/6.12.0/QtQuickControls2Imagine/private/qquickimaginestyle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickImagineStyle to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QObject, QUrl
  from ..QtQuickControls2 import QQuickAttachedPropertyPropagator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuickAttachedPropertyPropagator = WAIT['QQuickAttachedPropertyPropagator']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickImagineStyle(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickImagineStyle: a plain Python object standing in
  front of one C++ QQuickImagineStyle.

  What exists
  -----------

  Every function of Qt's QQuickImagineStyle that has a ritual and that Python
  can call so far, 12 names in all: 'metaObject', 'tr',
  'qmlAttachedProperties', 'path', 'setPath', 'inheritPath', 'propagatePath',
  'resetPath', 'url', 'pathChanged', 'attachedParentChange', 'init'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickImagineStyle::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickImagineStyle::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickImagineStyle::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'void QQuickImagineStyle::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickImagineStyle is created at the first use, not by
    'QQuickImagineStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickImagineStyle.
  - Qt tells when it has removed the C++ QQuickImagineStyle. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickImagineStyle::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimaginestyle.html#tr

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
    #  QString QQuickImagineStyle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickImagineStyle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickImagineStyle]:
    """
    Calls Qt's 'QQuickImagineStyle
    *QQuickImagineStyle::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimaginestyle.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickImagineStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickImagineStyle *QQuickImagineStyle::qmlAttachedProperties(QObject
    #      *object)
    address = Rituals.call(
        'ritual_ZN18QQuickImagineStyle21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    return QQuickImagineStyle._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickImagineStyle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickImagineStyle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimaginestyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickImagineStyle::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickImagineStyle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def path(self) -> str:
    """
    Calls Qt's 'QString QQuickImagineStyle::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimaginestyle.html#path

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickImagineStyle::path() const
    return self.uglySide.call('ritual_ZNK18QQuickImagineStyle4pathEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickImagineStyle::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimaginestyle.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickImagineStyle::url() const
    address = self.uglySide.call('ritual_ZNK18QQuickImagineStyle3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPath(self, path: str) -> None:
    """
    Calls Qt's 'void QQuickImagineStyle::setPath(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimaginestyle.html#setPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickImagineStyle::setPath(const QString &path)
    self.uglySide.call(
        'ritual_ZN18QQuickImagineStyle7setPathERK7QString', path,
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
    'QQuickImagineStyle::QQuickImagineStyle(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimaginestyle.html#QQuickImagineStyle

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickImagineStyle::QQuickImagineStyle(QObject *parent)
    self._noteCreation(QQuickImagineStyle, lambda: Rituals.call(
        'ritual_ZN18QQuickImagineStyleC1EP7QObject',
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

  @overload(str)
  def inheritPath(self, path: str) -> None:
    """
    Calls Qt's 'void QQuickImagineStyle::inheritPath(const QString &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimaginestyle.html#inheritPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickImagineStyle::inheritPath(const QString &path)
    self.uglySide.call(
        'ritual_ZN18QQuickImagineStyle11inheritPathERK7QString', path,
    )

  def propagatePath(self) -> None:
    """
    Calls Qt's 'void QQuickImagineStyle::propagatePath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimaginestyle.html#propagatePath
    """
    #  void QQuickImagineStyle::propagatePath()
    self.uglySide.call('ritual_ZN18QQuickImagineStyle13propagatePathEv')

  def resetPath(self) -> None:
    """
    Calls Qt's 'void QQuickImagineStyle::resetPath()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimaginestyle.html#resetPath
    """
    #  void QQuickImagineStyle::resetPath()
    self.uglySide.call('ritual_ZN18QQuickImagineStyle9resetPathEv')

  def pathChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImagineStyle::pathChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimaginestyle.html#pathChanged
    """
    #  void QQuickImagineStyle::pathChanged()
    self.uglySide.call('ritual_ZN18QQuickImagineStyle11pathChangedEv')

  @overload(
      QQuickAttachedPropertyPropagator, QQuickAttachedPropertyPropagator,
  )
  @overload(QQuickAttachedPropertyPropagator, NoneType)
  @overload(NoneType, QQuickAttachedPropertyPropagator)
  @overload(NoneType, NoneType)
  def attachedParentChange(
      self,
      newParent: Optional[QQuickAttachedPropertyPropagator],
      oldParent: Optional[QQuickAttachedPropertyPropagator],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickImagineStyle::attachedParentChange(QQuickAttachedPropertyPropagator
    *newParent, QQuickAttachedPropertyPropagator *oldParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimaginestyle.html#attachedParentChange

    Parameters
    ----------

    newParent : Optional[QQuickAttachedPropertyPropagator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldParent : Optional[QQuickAttachedPropertyPropagator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickImagineStyle::attachedParentChange(
    #      QQuickAttachedPropertyPropagator *newParent,
    #      QQuickAttachedPropertyPropagator *oldParent)
    ritual = (
        'ritual_ZN18QQuickImagineStyle20attachedParentChangeEP32QQuickAttac'
        'hedPropertyPropagatorS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickImagineStyle20attachedParentChangeEP32QQuic'
          'kAttachedPropertyPropagatorS1_')
    self.uglySide.call(
        ritual, self._addressOf(newParent), self._addressOf(oldParent),
    )

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickImagineStyle::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimaginestyle.html#init
    """
    #  void QQuickImagineStyle::init()
    self.uglySide.call('ritual_ZN18QQuickImagineStyle4initEv')
