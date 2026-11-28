"""
QQuickMessageDialogImplAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickmessagedialogimpl_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickMessageDialogImplAttached to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickMessageDialogImplAttachedPrivate
  from ..QtQuickTemplates2 import QQuickButton, QQuickDialogButtonBox
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickButton = WAIT['QQuickButton']
  QQuickDialogButtonBox = WAIT['QQuickDialogButtonBox']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMessageDialogImplAttached(QObject):
  """
  The cute side of Qt's QQuickMessageDialogImplAttached: a plain Python
  object standing in front of one C++ QQuickMessageDialogImplAttached.

  It is built on the cute 'QObject', as Qt's QQuickMessageDialogImplAttached
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMessageDialogImplAttached that has a ritual
  and that Python can call so far, 9 names in all: 'metaObject', 'tr',
  'buttonBox', 'setButtonBox', 'detailedTextButton', 'setDetailedTextButton',
  'buttonBoxChanged', 'detailedTextButtonChanged', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMessageDialogImplAttached::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuickMessageDialogImplAttached::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickMessageDialogImplAttachedPrivate
    *QQuickMessageDialogImplAttached::d_func() const': takes in Python what
    'QQuickMessageDialogImplAttachedPrivate
    *QQuickMessageDialogImplAttached::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickMessageDialogImplAttached is created at the first use, not
    by 'QQuickMessageDialogImplAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMessageDialogImplAttached.
  - Qt tells when it has removed the C++ QQuickMessageDialogImplAttached.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickMessageDialogImplAttached::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimplattached.html#tr

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
    #  QString QQuickMessageDialogImplAttached::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN31QQuickMessageDialogImplAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMessageDialogImplAttached'

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
    *QQuickMessageDialogImplAttached::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimplattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMessageDialogImplAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickMessageDialogImplAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def buttonBox(self) -> Optional[QQuickDialogButtonBox]:
    """
    Calls Qt's 'QQuickDialogButtonBox
    *QQuickMessageDialogImplAttached::buttonBox() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimplattached.html#buttonBox

    Returns
    -------

    Optional[QQuickDialogButtonBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialogButtonBox *QQuickMessageDialogImplAttached::buttonBox()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickMessageDialogImplAttached9buttonBoxEv',
    )
    from ..QtQuickTemplates2 import QQuickDialogButtonBox
    return QQuickDialogButtonBox._cuteAt(address)

  def detailedTextButton(self) -> Optional[QQuickButton]:
    """
    Calls Qt's 'QQuickButton
    *QQuickMessageDialogImplAttached::detailedTextButton() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimplattached.html

    Returns
    -------

    Optional[QQuickButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickButton *QQuickMessageDialogImplAttached::detailedTextButton()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickMessageDialogImplAttached18detailedTextButtonEv',
    )
    from ..QtQuickTemplates2 import QQuickButton
    return QQuickButton._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickDialogButtonBox)
  @overload(NoneType)
  def setButtonBox(self, buttons: Optional[QQuickDialogButtonBox]) -> None:
    """
    Calls Qt's 'void
    QQuickMessageDialogImplAttached::setButtonBox(QQuickDialogButtonBox
    *buttons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimplattached.html#setButtonBox

    Parameters
    ----------

    buttons : Optional[QQuickDialogButtonBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMessageDialogImplAttached::setButtonBox(
    #      QQuickDialogButtonBox *buttons)
    self.uglySide.call(
        'ritual_ZN31QQuickMessageDialogImplAttached12setButtonBoxEP21QQuick'
        'DialogButtonBox',
        self._addressOf(buttons),
    )

  @overload(QQuickButton)
  @overload(NoneType)
  def setDetailedTextButton(
      self,
      detailedTextButton: Optional[QQuickButton],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickMessageDialogImplAttached::setDetailedTextButton(QQuickButton
    *detailedTextButton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimplattached.html

    Parameters
    ----------

    detailedTextButton : Optional[QQuickButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMessageDialogImplAttached::setDetailedTextButton(
    #      QQuickButton *detailedTextButton)
    self.uglySide.call(
        'ritual_ZN31QQuickMessageDialogImplAttached21setDetailedTextButtonE'
        'P12QQuickButton',
        self._addressOf(detailedTextButton),
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
    'QQuickMessageDialogImplAttached::QQuickMessageDialogImplAttached(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimplattached.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickMessageDialogImplAttached::QQuickMessageDialogImplAttached(
    #      QObject *parent)
    self._noteCreation(QQuickMessageDialogImplAttached, lambda: Rituals.call(
        'ritual_ZN31QQuickMessageDialogImplAttachedC1EP7QObject',
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

  def buttonBoxChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMessageDialogImplAttached::buttonBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimplattached.html
    """
    #  void QQuickMessageDialogImplAttached::buttonBoxChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickMessageDialogImplAttached16buttonBoxChangedEv',
    )

  def detailedTextButtonChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickMessageDialogImplAttached::detailedTextButtonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimplattached.html
    """
    #  void QQuickMessageDialogImplAttached::detailedTextButtonChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickMessageDialogImplAttached25detailedTextButtonChan'
        'gedEv',
    )

  def d_func(self) -> Optional[QQuickMessageDialogImplAttachedPrivate]:
    """
    Calls Qt's 'QQuickMessageDialogImplAttachedPrivate
    *QQuickMessageDialogImplAttached::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialogimplattached.html#d_func

    Returns
    -------

    Optional[QQuickMessageDialogImplAttachedPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMessageDialogImplAttachedPrivate
    #      *QQuickMessageDialogImplAttached::d_func()
    address = self.uglySide.call(
        'ritual_ZN31QQuickMessageDialogImplAttached6d_funcEv',
    )
    from . import QQuickMessageDialogImplAttachedPrivate
    return QQuickMessageDialogImplAttachedPrivate._cuteAt(address)
