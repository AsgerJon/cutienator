"""
QQuickFontDialogImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfontdialogimpl_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFontDialogImpl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QObject
  from ..QtGui import QFocusEvent, QFont, QKeyEvent
  from . import QQuickFontDialogImplAttached, QQuickFontDialogImplPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFocusEvent = WAIT['QFocusEvent']
  QFont = WAIT['QFont']
  QKeyEvent = WAIT['QKeyEvent']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFontDialogImpl(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickFontDialogImpl: a plain Python object standing
  in front of one C++ QQuickFontDialogImpl.

  What exists
  -----------

  Every function of Qt's QQuickFontDialogImpl that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr',
  'qmlAttachedProperties', 'currentFont', 'setCurrentFont', 'init',
  'optionsChanged', 'currentFontChanged', 'keyReleaseEvent', 'focusOutEvent',
  'itemChange', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFontDialogImpl::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickFontDialogImpl::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickFontDialogImpl::qt_qmlMarker_attached()': one of Qt's
    own inner workings.
  - Qt's 'QSharedPointer<QFontDialogOptions> QQuickFontDialogImpl::options()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QQuickFontDialogImpl::setOptions(const
    QSharedPointer<QFontDialogOptions> &options)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QQuickFontDialogImplPrivate *QQuickFontDialogImpl::d_func()
    const': takes in Python what 'QQuickFontDialogImplPrivate
    *QQuickFontDialogImpl::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickFontDialogImpl is created at the first use, not by
    'QQuickFontDialogImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFontDialogImpl.
  - Qt tells when it has removed the C++ QQuickFontDialogImpl. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickFontDialogImpl that has no cute function yet,
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
    Calls Qt's 'QString QQuickFontDialogImpl::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontdialogimpl.html#tr

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
    #  QString QQuickFontDialogImpl::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickFontDialogImpl2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickFontDialogImplAttached]:
    """
    Calls Qt's 'QQuickFontDialogImplAttached
    *QQuickFontDialogImpl::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimpl.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickFontDialogImplAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFontDialogImplAttached
    #      *QQuickFontDialogImpl::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN20QQuickFontDialogImpl21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickFontDialogImplAttached
    return QQuickFontDialogImplAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFontDialogImpl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFontDialogImpl::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimpl.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFontDialogImpl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickFontDialogImpl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickFontDialogImpl::currentFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimpl.html#currentFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickFontDialogImpl::currentFont() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickFontDialogImpl11currentFontEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  @overload(QFont, bool)
  def setCurrentFont(
      self,
      font: QFont,
      selectInListViews: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImpl::setCurrentFont(const QFont &font,
    bool selectInListViews)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimpl.html#setCurrentFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    selectInListViews : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickFontDialogImpl::setCurrentFont(const QFont &font, bool
    #      selectInListViews)
    self.uglySide.call(
        'ritual_ZN20QQuickFontDialogImpl14setCurrentFontERK5QFontb',
        self._valueOf(font), selectInListViews,
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
    'QQuickFontDialogImpl::QQuickFontDialogImpl(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimpl.html#QQuickFontDialogImpl

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFontDialogImpl::QQuickFontDialogImpl(QObject *parent)
    self._noteCreation(QQuickFontDialogImpl, lambda: Rituals.call(
        'ritual_ZN20QQuickFontDialogImplC1EP7QObject',
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

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImpl::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontdialogimpl.html#init
    """
    #  void QQuickFontDialogImpl::init()
    self.uglySide.call('ritual_ZN20QQuickFontDialogImpl4initEv')

  def optionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImpl::optionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimpl.html#optionsChanged
    """
    #  void QQuickFontDialogImpl::optionsChanged()
    self.uglySide.call('ritual_ZN20QQuickFontDialogImpl14optionsChangedEv')

  @overload(QFont)
  def currentFontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImpl::currentFontChanged(const QFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimpl.html#currentFontChanged

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickFontDialogImpl::currentFontChanged(const QFont &font)
    self.uglySide.call(
        'ritual_ZN20QQuickFontDialogImpl18currentFontChangedERK5QFont',
        self._valueOf(font),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImpl::keyReleaseEvent(QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimpl.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFontDialogImpl::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN20QQuickFontDialogImpl15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickFontDialogImpl15keyReleaseEventEP9QKeyEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImpl::focusOutEvent(QFocusEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimpl.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFontDialogImpl::focusOutEvent(QFocusEvent *event)
    ritual = 'ritual_ZN20QQuickFontDialogImpl13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickFontDialogImpl13focusOutEventEP11QFocusEven'
          't')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImpl::itemChange(QQuickItem::ItemChange
    change, const QQuickItem::ItemChangeData &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimpl.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickFontDialogImpl::itemChange(QQuickItem::ItemChange change,
    #      const QQuickItem::ItemChangeData &data)
    ritual = (
        'ritual_ZN20QQuickFontDialogImpl10itemChangeEN10QQuickItem10ItemCha'
        'ngeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickFontDialogImpl10itemChangeEN10QQuickItem10I'
          'temChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  def d_func(self) -> Optional[QQuickFontDialogImplPrivate]:
    """
    Calls Qt's 'QQuickFontDialogImplPrivate *QQuickFontDialogImpl::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontdialogimpl.html#d_func

    Returns
    -------

    Optional[QQuickFontDialogImplPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFontDialogImplPrivate *QQuickFontDialogImpl::d_func()
    address = self.uglySide.call('ritual_ZN20QQuickFontDialogImpl6d_funcEv')
    from . import QQuickFontDialogImplPrivate
    return QQuickFontDialogImplPrivate._cuteAt(address)

  @staticmethod
  def options(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QFontDialogOptions> QQuickFontDialogImpl::options()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickFontDialogImpl.options' has no cute function yet. Qt's "
        "'QSharedPointer<QFontDialogOptions> "
        "QQuickFontDialogImpl::options() const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def setOptions(*__, **_) -> Never:
    """
    Qt's 'void QQuickFontDialogImpl::setOptions(const
    QSharedPointer<QFontDialogOptions> &options)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickFontDialogImpl.setOptions' has no cute function yet. Qt's "
        "'void QQuickFontDialogImpl::setOptions(const "
        "QSharedPointer<QFontDialogOptions> &options)': takes a type Python "
        "has no way to hand over yet.")
