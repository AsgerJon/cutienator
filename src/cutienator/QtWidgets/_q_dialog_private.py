"""
QDialogPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qdialog_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDialogPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QPlatformDialogHelper
from . import QDialog, QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from ..QtGui import QWindow
  from . import QPushButton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPushButton = WAIT['QPushButton']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDialogPrivate(QWidgetPrivate):
  """
  The cute side of Qt's QDialogPrivate: a plain Python object standing in
  front of one C++ QDialogPrivate.

  It is built on the cute 'QWidgetPrivate', as Qt's QDialogPrivate is built
  on Qt's QWidgetPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDialogPrivate that has a ritual and that Python can
  call so far, 17 names in all: 'q_func', 'setVisible',
  'transientParentWindow', 'setNativeDialogVisible', 'styleHint',
  'setDefault', 'setMainDefault', 'hideDefault', 'resetModalitySetByOpen',
  'platformHelper', 'canBeNativeDialog', 'close', 'recreate', 'dialogCode',
  'initHelper', 'helperPrepareShow', 'helperDone'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QDialog *QDialogPrivate::q_func() const': takes in Python
    what 'QDialog *QDialogPrivate::q_func()' takes.
  - Qt's 'QDialogPrivate::~QDialogPrivate()': the destructor: Python never
    removes a C++ QDialogPrivate.

  What to expect
  --------------

  - The C++ QDialogPrivate is created at the first use, not by
    'QDialogPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDialogPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDialogPrivate'

  #  A C++ QDialogPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDialogPrivate'

  #  The functions Qt calls itself that QDialogPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'canBeNativeDialog': (
          ('_ZNK14QDialogPrivate17canBeNativeDialogEv',
           ('bool', 'number', ''),
           ()),
      ),
      'dialogCode': (
          ('_ZNK14QDialogPrivate10dialogCodeEv',
           ('int', 'number', ''),
           ()),
      ),
      'initHelper': (
          ('_ZN14QDialogPrivate10initHelperEP21QPlatformDialogHelper',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformDialogHelper'),
           )),
      ),
      'helperPrepareShow': (
          ('_ZN14QDialogPrivate17helperPrepareShowEP21QPlatformDialogHelper',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformDialogHelper'),
           )),
      ),
      'helperDone': (
          ('_ZN14QDialogPrivate10helperDoneEN7QDialog10DialogCodeEP21QPlatf'
           'ormDialogHelper',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtWidgets:QDialog.DialogCode'),
               ('address', 'address', 'QtGui:QPlatformDialogHelper'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def transientParentWindow(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QDialogPrivate::transientParentWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogprivate.html#transientParentWindow

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QDialogPrivate::transientParentWindow() const
    address = self.uglySide.call(
        'ritual_ZNK14QDialogPrivate21transientParentWindowEv',
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  @overload(QPlatformDialogHelper.StyleHint)
  def styleHint(self, hint: QPlatformDialogHelper.StyleHint) -> QVariant:
    """
    Calls Qt's 'QVariant
    QDialogPrivate::styleHint(QPlatformDialogHelper::StyleHint hint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogprivate.html#styleHint

    Parameters
    ----------

    hint : QPlatformDialogHelper.StyleHint
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDialogPrivate::styleHint(QPlatformDialogHelper::StyleHint
    #      hint) const
    address = self.uglySide.call(
        'ritual_ZNK14QDialogPrivate9styleHintEN21QPlatformDialogHelper9Styl'
        'eHintE',
        hint.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def platformHelper(self) -> Optional[QPlatformDialogHelper]:
    """
    Calls Qt's 'QPlatformDialogHelper *QDialogPrivate::platformHelper()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogprivate.html#platformHelper

    Returns
    -------

    Optional[QPlatformDialogHelper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformDialogHelper *QDialogPrivate::platformHelper() const
    address = self.uglySide.call(
        'ritual_ZNK14QDialogPrivate14platformHelperEv',
    )
    return QPlatformDialogHelper._cuteAt(address)

  def canBeNativeDialog(self) -> bool:
    """
    Calls Qt's 'bool QDialogPrivate::canBeNativeDialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogprivate.html#canBeNativeDialog
    """
    #  bool QDialogPrivate::canBeNativeDialog() const
    ritual = 'ritual_ZNK14QDialogPrivate17canBeNativeDialogEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QDialogPrivate17canBeNativeDialogEv'
    return self.uglySide.call(ritual)

  def dialogCode(self) -> int:
    """
    Calls Qt's 'int QDialogPrivate::dialogCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogprivate.html#dialogCode
    """
    #  int QDialogPrivate::dialogCode() const
    ritual = 'ritual_ZNK14QDialogPrivate10dialogCodeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QDialogPrivate10dialogCodeEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QDialogPrivate::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogprivate.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QDialogPrivate::setVisible(bool visible)
    ritual = 'ritual_ZN14QDialogPrivate10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QDialogPrivate10setVisibleEb'
    self.uglySide.call(ritual, visible)

  @overload(bool)
  def setNativeDialogVisible(self, visible: bool) -> bool:
    """
    Calls Qt's 'bool QDialogPrivate::setNativeDialogVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogprivate.html#setNativeDialogVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  bool QDialogPrivate::setNativeDialogVisible(bool visible)
    return self.uglySide.call(
        'ritual_ZN14QDialogPrivate22setNativeDialogVisibleEb', visible,
    )

  @overload(QPushButton)
  @overload(NoneType)
  def setDefault(self, a0: Optional[QPushButton]) -> None:
    """
    Calls Qt's 'void QDialogPrivate::setDefault(QPushButton *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogprivate.html#setDefault

    Parameters
    ----------

    a0 : Optional[QPushButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDialogPrivate::setDefault(QPushButton *a0)
    self.uglySide.call(
        'ritual_ZN14QDialogPrivate10setDefaultEP11QPushButton',
        self._addressOf(a0),
    )

  @overload(QPushButton)
  @overload(NoneType)
  def setMainDefault(self, a0: Optional[QPushButton]) -> None:
    """
    Calls Qt's 'void QDialogPrivate::setMainDefault(QPushButton *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogprivate.html#setMainDefault

    Parameters
    ----------

    a0 : Optional[QPushButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDialogPrivate::setMainDefault(QPushButton *a0)
    self.uglySide.call(
        'ritual_ZN14QDialogPrivate14setMainDefaultEP11QPushButton',
        self._addressOf(a0),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QDialogPrivate::QDialogPrivate()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdialogprivate.html#QDialogPrivate
    """
    #  QDialogPrivate::QDialogPrivate()
    self._noteCreation(QDialogPrivate, lambda: Rituals.call(
        'ritual_ZN14QDialogPrivateC1Ev',
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

  def q_func(self) -> Optional[QDialog]:
    """
    Calls Qt's 'QDialog *QDialogPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogprivate.html#q_func

    Returns
    -------

    Optional[QDialog]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDialog *QDialogPrivate::q_func()
    address = self.uglySide.call('ritual_ZN14QDialogPrivate6q_funcEv')
    return QDialog._cuteAt(address)

  def hideDefault(self) -> None:
    """
    Calls Qt's 'void QDialogPrivate::hideDefault()'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogprivate.html#hideDefault
    """
    #  void QDialogPrivate::hideDefault()
    self.uglySide.call('ritual_ZN14QDialogPrivate11hideDefaultEv')

  def resetModalitySetByOpen(self) -> None:
    """
    Calls Qt's 'void QDialogPrivate::resetModalitySetByOpen()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogprivate.html#resetModalitySetByOpen
    """
    #  void QDialogPrivate::resetModalitySetByOpen()
    self.uglySide.call('ritual_ZN14QDialogPrivate22resetModalitySetByOpenEv')

  @overload(int)
  def close(self, resultCode: int) -> None:
    """
    Calls Qt's 'void QDialogPrivate::close(int resultCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogprivate.html#close

    Parameters
    ----------

    resultCode : int
      Passed on as it is.
    """
    #  void QDialogPrivate::close(int resultCode)
    self.uglySide.call('ritual_ZN14QDialogPrivate5closeEi', resultCode)

  def recreate(self) -> None:
    """
    Calls Qt's 'void QDialogPrivate::recreate()'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogprivate.html#recreate
    """
    #  void QDialogPrivate::recreate()
    ritual = 'ritual_ZN14QDialogPrivate8recreateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QDialogPrivate8recreateEv'
    self.uglySide.call(ritual)

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def initHelper(self, a0: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QDialogPrivate::initHelper(QPlatformDialogHelper *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogprivate.html#initHelper

    Parameters
    ----------

    a0 : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDialogPrivate::initHelper(QPlatformDialogHelper *a0)
    ritual = 'ritual_ZN14QDialogPrivate10initHelperEP21QPlatformDialogHelper'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QDialogPrivate10initHelperEP21QPlatformDialogHelp'
          'er')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def helperPrepareShow(self, a0: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QDialogPrivate::helperPrepareShow(QPlatformDialogHelper
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogprivate.html#helperPrepareShow

    Parameters
    ----------

    a0 : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDialogPrivate::helperPrepareShow(QPlatformDialogHelper *a0)
    ritual = (
        'ritual_ZN14QDialogPrivate17helperPrepareShowEP21QPlatformDialogHel'
        'per')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QDialogPrivate17helperPrepareShowEP21QPlatformDia'
          'logHelper')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDialog.DialogCode, QPlatformDialogHelper)
  @overload(QDialog.DialogCode, NoneType)
  def helperDone(
      self,
      a0: QDialog.DialogCode,
      a1: Optional[QPlatformDialogHelper],
  ) -> None:
    """
    Calls Qt's 'void QDialogPrivate::helperDone(QDialog::DialogCode a0,
    QPlatformDialogHelper *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogprivate.html#helperDone

    Parameters
    ----------

    a0 : QDialog.DialogCode
      Passed on as its number.

    a1 : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDialogPrivate::helperDone(QDialog::DialogCode a0,
    #      QPlatformDialogHelper *a1)
    ritual = (
        'ritual_ZN14QDialogPrivate10helperDoneEN7QDialog10DialogCodeEP21QPl'
        'atformDialogHelper')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QDialogPrivate10helperDoneEN7QDialog10DialogCodeE'
          'P21QPlatformDialogHelper')
    self.uglySide.call(ritual, a0.value, self._addressOf(a1))
