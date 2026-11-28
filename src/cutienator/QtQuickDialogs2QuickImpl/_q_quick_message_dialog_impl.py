"""
QQuickMessageDialogImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickmessagedialogimpl_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickMessageDialogImpl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QPlatformDialogHelper
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QObject
  from . import QQuickMessageDialogImplAttached
  from . import QQuickMessageDialogImplPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMessageDialogImpl(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickMessageDialogImpl: a plain Python object
  standing in front of one C++ QQuickMessageDialogImpl.

  What exists
  -----------

  Every function of Qt's QQuickMessageDialogImpl that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr',
  'qmlAttachedProperties', 'showDetailedText', 'text', 'informativeText',
  'detailedText', 'buttonClicked', 'showDetailedTextChanged',
  'optionsChanged', 'toggleShowDetailedText', 'itemChange', 'd_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMessageDialogImpl::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickMessageDialogImpl::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickMessageDialogImpl::qt_qmlMarker_attached()': one of Qt's
    own inner workings.
  - Qt's 'QSharedPointer<QMessageDialogOptions>
    QQuickMessageDialogImpl::options() const': gives a type Python has no way
    to take yet.
  - Qt's 'void QQuickMessageDialogImpl::setOptions(const
    QSharedPointer<QMessageDialogOptions> &options)': takes a type Python has
    no way to hand over yet.
  - Qt's 'const QQuickMessageDialogImplPrivate
    *QQuickMessageDialogImpl::d_func() const': takes in Python what
    'QQuickMessageDialogImplPrivate *QQuickMessageDialogImpl::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickMessageDialogImpl is created at the first use, not by
    'QQuickMessageDialogImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMessageDialogImpl.
  - Qt tells when it has removed the C++ QQuickMessageDialogImpl. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickMessageDialogImpl that has no cute function yet,
    'options', 'setOptions', holds a function that raises
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
    Calls Qt's 'QString QQuickMessageDialogImpl::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmessagedialogimpl.html#tr

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
    #  QString QQuickMessageDialogImpl::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickMessageDialogImpl2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickMessageDialogImplAttached]:
    """
    Calls Qt's 'QQuickMessageDialogImplAttached
    *QQuickMessageDialogImpl::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimpl.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickMessageDialogImplAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMessageDialogImplAttached
    #      *QQuickMessageDialogImpl::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN23QQuickMessageDialogImpl21qmlAttachedPropertiesEP7QObjec'
        't',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickMessageDialogImplAttached
    return QQuickMessageDialogImplAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMessageDialogImpl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMessageDialogImpl::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimpl.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMessageDialogImpl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickMessageDialogImpl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def showDetailedText(self) -> bool:
    """
    Calls Qt's 'bool QQuickMessageDialogImpl::showDetailedText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimpl.html#showDetailedText
    """
    #  bool QQuickMessageDialogImpl::showDetailedText() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickMessageDialogImpl16showDetailedTextEv',
    )

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickMessageDialogImpl::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmessagedialogimpl.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickMessageDialogImpl::text() const
    return self.uglySide.call('ritual_ZNK23QQuickMessageDialogImpl4textEv')

  def informativeText(self) -> str:
    """
    Calls Qt's 'QString QQuickMessageDialogImpl::informativeText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimpl.html#informativeText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickMessageDialogImpl::informativeText() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickMessageDialogImpl15informativeTextEv',
    )

  def detailedText(self) -> str:
    """
    Calls Qt's 'QString QQuickMessageDialogImpl::detailedText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimpl.html#detailedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickMessageDialogImpl::detailedText() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickMessageDialogImpl12detailedTextEv',
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickMessageDialogImpl::QQuickMessageDialogImpl(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimpl.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickMessageDialogImpl::QQuickMessageDialogImpl(QObject *parent)
    self._noteCreation(QQuickMessageDialogImpl, lambda: Rituals.call(
        'ritual_ZN23QQuickMessageDialogImplC1EP7QObject',
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

  @overload(
      QPlatformDialogHelper.StandardButton, QPlatformDialogHelper.ButtonRole,
  )
  def buttonClicked(
      self,
      button: QPlatformDialogHelper.StandardButton,
      role: QPlatformDialogHelper.ButtonRole,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickMessageDialogImpl::buttonClicked(QPlatformDialogHelper::
    StandardButton button, QPlatformDialogHelper::ButtonRole role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimpl.html#buttonClicked

    Parameters
    ----------

    button : QPlatformDialogHelper.StandardButton
      Passed on as its number.

    role : QPlatformDialogHelper.ButtonRole
      Passed on as its number.
    """
    #  void QQuickMessageDialogImpl::buttonClicked(QPlatformDialogHelper::
    #      StandardButton button, QPlatformDialogHelper::ButtonRole role)
    self.uglySide.call(
        'ritual_ZN23QQuickMessageDialogImpl13buttonClickedEN21QPlatformDial'
        'ogHelper14StandardButtonENS0_10ButtonRoleE',
        button.value, role.value,
    )

  def showDetailedTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMessageDialogImpl::showDetailedTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimpl.html
    """
    #  void QQuickMessageDialogImpl::showDetailedTextChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickMessageDialogImpl23showDetailedTextChangedEv',
    )

  def optionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMessageDialogImpl::optionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimpl.html#optionsChanged
    """
    #  void QQuickMessageDialogImpl::optionsChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickMessageDialogImpl14optionsChangedEv',
    )

  def toggleShowDetailedText(self) -> None:
    """
    Calls Qt's 'void QQuickMessageDialogImpl::toggleShowDetailedText()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimpl.html
    """
    #  void QQuickMessageDialogImpl::toggleShowDetailedText()
    self.uglySide.call(
        'ritual_ZN23QQuickMessageDialogImpl22toggleShowDetailedTextEv',
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickMessageDialogImpl::itemChange(QQuickItem::ItemChange change, const
    QQuickItem::ItemChangeData &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimpl.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickMessageDialogImpl::itemChange(QQuickItem::ItemChange
    #      change, const QQuickItem::ItemChangeData &data)
    ritual = (
        'ritual_ZN23QQuickMessageDialogImpl10itemChangeEN10QQuickItem10Item'
        'ChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuickMessageDialogImpl10itemChangeEN10QQuickItem'
          '10ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  def d_func(self) -> Optional[QQuickMessageDialogImplPrivate]:
    """
    Calls Qt's 'QQuickMessageDialogImplPrivate
    *QQuickMessageDialogImpl::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimpl.html#d_func

    Returns
    -------

    Optional[QQuickMessageDialogImplPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMessageDialogImplPrivate *QQuickMessageDialogImpl::d_func()
    address = self.uglySide.call(
        'ritual_ZN23QQuickMessageDialogImpl6d_funcEv',
    )
    from . import QQuickMessageDialogImplPrivate
    return QQuickMessageDialogImplPrivate._cuteAt(address)

  @staticmethod
  def options(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QMessageDialogOptions>
    QQuickMessageDialogImpl::options() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQuickMessageDialogImpl.options' has no cute function yet. Qt's "
        "'QSharedPointer<QMessageDialogOptions> "
        "QQuickMessageDialogImpl::options() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def setOptions(*__, **_) -> Never:
    """
    Qt's 'void QQuickMessageDialogImpl::setOptions(const
    QSharedPointer<QMessageDialogOptions> &options)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickMessageDialogImpl.setOptions' has no cute function yet. "
        "Qt's 'void QQuickMessageDialogImpl::setOptions(const "
        "QSharedPointer<QMessageDialogOptions> &options)': takes a type "
        "Python has no way to hand over yet.")
