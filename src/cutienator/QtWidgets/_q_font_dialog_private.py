"""
QFontDialogPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qfontdialog_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QFontDialogPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QDialogPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QFont, QPlatformDialogHelper, QPlatformFontDialogHelper
  from . import QFontDialog
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QPlatformDialogHelper = WAIT['QPlatformDialogHelper']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFontDialogPrivate(QDialogPrivate):
  """
  The cute side of Qt's QFontDialogPrivate: a plain Python object standing in
  front of one C++ QFontDialogPrivate.

  It is built on the cute 'QDialogPrivate', as Qt's QFontDialogPrivate is
  built on Qt's QDialogPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFontDialogPrivate that has a ritual and that Python
  can call so far, 9 names in all: 'q_func', 'platformFontDialogHelper',
  'writingSystemHighlighted', 'updateSampleFont', 'retranslateStrings',
  'canBeNativeDialog', 'setVisible', 'initHelper', 'helperPrepareShow'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QFontDialog *QFontDialogPrivate::q_func() const': takes in
    Python what 'QFontDialog *QFontDialogPrivate::q_func()' takes.
  - Qt's 'QFontDialogPrivate::~QFontDialogPrivate()': the destructor: Python
    never removes a C++ QFontDialogPrivate.
  - Qt's 'QFont QFontDialogPrivate::getFont(bool *ok, const QFont &initial,
    QWidget *parent, const QString &title, QFontDialog::FontDialogOptions
    options)': takes a number to change where it is.

  What has no ritual
  ------------------

  10 of the 23 functions Qt declares: 9 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 cannot be
  called and cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QFontDialogPrivate is created at the first use, not by
    'QFontDialogPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFontDialogPrivate.
  - Each name of Qt's QFontDialogPrivate that has no cute function yet,
    '_q_runNativeAppModalPanel', 'familyHighlighted', 'getFont',
    'sizeChanged', 'sizeHighlighted', 'styleHighlighted', 'updateFamilies',
    'updateSample', 'updateSizes', 'updateStyles', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontDialogPrivate'

  #  A C++ QFontDialogPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFontDialogPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def platformFontDialogHelper(self) -> Optional[QPlatformFontDialogHelper]:
    """
    Calls Qt's 'QPlatformFontDialogHelper
    *QFontDialogPrivate::platformFontDialogHelper() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdialogprivate.html#platformFontDialogHelper

    Returns
    -------

    Optional[QPlatformFontDialogHelper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformFontDialogHelper
    #      *QFontDialogPrivate::platformFontDialogHelper() const
    address = self.uglySide.call(
        'ritual_ZNK18QFontDialogPrivate24platformFontDialogHelperEv',
    )
    from ..QtGui import QPlatformFontDialogHelper
    return QPlatformFontDialogHelper._cuteAt(address)

  def canBeNativeDialog(self) -> bool:
    """
    Calls Qt's 'bool QFontDialogPrivate::canBeNativeDialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdialogprivate.html#canBeNativeDialog
    """
    #  bool QFontDialogPrivate::canBeNativeDialog() const
    ritual = 'ritual_ZNK18QFontDialogPrivate17canBeNativeDialogEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QFontDialogPrivate17canBeNativeDialogEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QFontDialogPrivate::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialogprivate.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QFontDialogPrivate::setVisible(bool visible)
    ritual = 'ritual_ZN18QFontDialogPrivate10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QFontDialogPrivate10setVisibleEb'
    self.uglySide.call(ritual, visible)

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
    'QFontDialogPrivate::QFontDialogPrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdialogprivate.html#QFontDialogPrivate
    """
    #  QFontDialogPrivate::QFontDialogPrivate()
    self._noteCreation(QFontDialogPrivate, lambda: Rituals.call(
        'ritual_ZN18QFontDialogPrivateC1Ev',
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

  def q_func(self) -> Optional[QFontDialog]:
    """
    Calls Qt's 'QFontDialog *QFontDialogPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialogprivate.html#q_func

    Returns
    -------

    Optional[QFontDialog]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontDialog *QFontDialogPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QFontDialogPrivate6q_funcEv')
    from . import QFontDialog
    return QFontDialog._cuteAt(address)

  @overload(int)
  def writingSystemHighlighted(self, a0: int) -> None:
    """
    Calls Qt's 'void QFontDialogPrivate::writingSystemHighlighted(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdialogprivate.html#writingSystemHighlighted

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QFontDialogPrivate::writingSystemHighlighted(int a0)
    self.uglySide.call(
        'ritual_ZN18QFontDialogPrivate24writingSystemHighlightedEi', a0,
    )

  @overload(QFont)
  def updateSampleFont(self, newFont: QFont) -> None:
    """
    Calls Qt's 'void QFontDialogPrivate::updateSampleFont(const QFont
    &newFont)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdialogprivate.html#updateSampleFont

    Parameters
    ----------

    newFont : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QFontDialogPrivate::updateSampleFont(const QFont &newFont)
    self.uglySide.call(
        'ritual_ZN18QFontDialogPrivate16updateSampleFontERK5QFont',
        self._valueOf(newFont),
    )

  def retranslateStrings(self) -> None:
    """
    Calls Qt's 'void QFontDialogPrivate::retranslateStrings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdialogprivate.html#retranslateStrings
    """
    #  void QFontDialogPrivate::retranslateStrings()
    self.uglySide.call('ritual_ZN18QFontDialogPrivate18retranslateStringsEv')

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def initHelper(self, a0: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QFontDialogPrivate::initHelper(QPlatformDialogHelper
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialogprivate.html#initHelper

    Parameters
    ----------

    a0 : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFontDialogPrivate::initHelper(QPlatformDialogHelper *a0)
    ritual = (
        'ritual_ZN18QFontDialogPrivate10initHelperEP21QPlatformDialogHelper')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QFontDialogPrivate10initHelperEP21QPlatformDialog'
          'Helper')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def helperPrepareShow(self, a0: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void
    QFontDialogPrivate::helperPrepareShow(QPlatformDialogHelper *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdialogprivate.html#helperPrepareShow

    Parameters
    ----------

    a0 : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFontDialogPrivate::helperPrepareShow(QPlatformDialogHelper *a0)
    ritual = (
        'ritual_ZN18QFontDialogPrivate17helperPrepareShowEP21QPlatformDialo'
        'gHelper')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QFontDialogPrivate17helperPrepareShowEP21QPlatfor'
          'mDialogHelper')
    self.uglySide.call(ritual, self._addressOf(a0))

  @staticmethod
  def _q_runNativeAppModalPanel(*__, **_) -> Never:
    """
    Qt's 'void QFontDialogPrivate::_q_runNativeAppModalPanel()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QFontDialogPrivate._q_runNativeAppModalPanel' has no cute "
        "function yet. Qt's 'void "
        "QFontDialogPrivate::_q_runNativeAppModalPanel()': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def familyHighlighted(*__, **_) -> Never:
    """
    Qt's 'void QFontDialogPrivate::familyHighlighted(int a0)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'QFontListView'.
    """
    raise NotImplementedError(
        "'QFontDialogPrivate.familyHighlighted' has no cute function yet. "
        "Qt's 'void QFontDialogPrivate::familyHighlighted(int a0)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QFontListView'.")

  @staticmethod
  def getFont(*__, **_) -> Never:
    """
    Qt's 'QFont QFontDialogPrivate::getFont(bool *ok, const QFont &initial,
    QWidget *parent, const QString &title, QFontDialog::FontDialogOptions
    options)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QFontDialogPrivate.getFont' has no cute function yet. Qt's 'QFont "
        "QFontDialogPrivate::getFont(bool *ok, const QFont &initial, "
        "QWidget *parent, const QString &title, "
        "QFontDialog::FontDialogOptions options)': takes a number to change "
        "where it is.")

  @staticmethod
  def sizeChanged(*__, **_) -> Never:
    """
    Qt's 'void QFontDialogPrivate::sizeChanged(const QString &a0)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'QFontListView'.
    """
    raise NotImplementedError(
        "'QFontDialogPrivate.sizeChanged' has no cute function yet. Qt's "
        "'void QFontDialogPrivate::sizeChanged(const QString &a0)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QFontListView'.")

  @staticmethod
  def sizeHighlighted(*__, **_) -> Never:
    """
    Qt's 'void QFontDialogPrivate::sizeHighlighted(int a0)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'QFontListView'.
    """
    raise NotImplementedError(
        "'QFontDialogPrivate.sizeHighlighted' has no cute function yet. "
        "Qt's 'void QFontDialogPrivate::sizeHighlighted(int a0)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QFontListView'.")

  @staticmethod
  def styleHighlighted(*__, **_) -> Never:
    """
    Qt's 'void QFontDialogPrivate::styleHighlighted(int a0)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'QFontListView'.
    """
    raise NotImplementedError(
        "'QFontDialogPrivate.styleHighlighted' has no cute function yet. "
        "Qt's 'void QFontDialogPrivate::styleHighlighted(int a0)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QFontListView'.")

  @staticmethod
  def updateFamilies(*__, **_) -> Never:
    """
    Qt's 'void QFontDialogPrivate::updateFamilies()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QFontListView'.
    """
    raise NotImplementedError(
        "'QFontDialogPrivate.updateFamilies' has no cute function yet. Qt's "
        "'void QFontDialogPrivate::updateFamilies()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'QFontListView'.")

  @staticmethod
  def updateSample(*__, **_) -> Never:
    """
    Qt's 'void QFontDialogPrivate::updateSample()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QFontListView'.
    """
    raise NotImplementedError(
        "'QFontDialogPrivate.updateSample' has no cute function yet. Qt's "
        "'void QFontDialogPrivate::updateSample()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'QFontListView'.")

  @staticmethod
  def updateSizes(*__, **_) -> Never:
    """
    Qt's 'void QFontDialogPrivate::updateSizes()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QFontListView'.
    """
    raise NotImplementedError(
        "'QFontDialogPrivate.updateSizes' has no cute function yet. Qt's "
        "'void QFontDialogPrivate::updateSizes()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: member access into incomplete type 'QFontListView'.")

  @staticmethod
  def updateStyles(*__, **_) -> Never:
    """
    Qt's 'void QFontDialogPrivate::updateStyles()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QFontListView'.
    """
    raise NotImplementedError(
        "'QFontDialogPrivate.updateStyles' has no cute function yet. Qt's "
        "'void QFontDialogPrivate::updateStyles()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'QFontListView'.")
