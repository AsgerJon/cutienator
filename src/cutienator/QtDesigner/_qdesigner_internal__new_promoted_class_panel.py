"""
qdesigner_internal::NewPromotedClassPanel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_promotiondialog_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means qdesigner_internal::NewPromotedClassPanel to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtWidgets import QGroupBox

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class NewPromotedClassPanel(QGroupBox):
  """
  The cute side of Qt's qdesigner_internal::NewPromotedClassPanel: a plain
  Python object standing in front of one C++
  qdesigner_internal::NewPromotedClassPanel.

  It is built on the cute 'QGroupBox', as Qt's
  qdesigner_internal::NewPromotedClassPanel is built on Qt's QGroupBox, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::NewPromotedClassPanel that has a
  ritual and that Python can call so far, 12 names in all: 'metaObject',
  'promotedHeaderSuffix', 'setPromotedHeaderSuffix',
  'isPromotedHeaderLowerCase', 'setPromotedHeaderLowerCase', 'grabFocus',
  'chooseBaseClass', 'slotNameChanged', 'slotIncludeFileChanged', 'slotAdd',
  'slotReset', 'enableButtons'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::NewPromotedClassPanel::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::NewPromotedClassPanel::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  6 of the 20 functions Qt declares: 2 not a gap; 2 the compiler refuses its
  ritual as it would be written here; 2 leans on 'qdesigner_internal.

  What to expect
  --------------

  - The C++ qdesigner_internal::NewPromotedClassPanel is created at the first
    use, not by 'qdesigner_internal::NewPromotedClassPanel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::NewPromotedClassPanel.
  - Qt tells when it has removed the C++
    qdesigner_internal::NewPromotedClassPanel. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  - Each name of Qt's qdesigner_internal::NewPromotedClassPanel that has no
    cute function yet, '__init__', 'newPromotedClass', 'promotionParameters',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::NewPromotedClassPanel'

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
    *qdesigner_internal::NewPromotedClassPanel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newpromotedclasspanel.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *qdesigner_internal::NewPromotedClassPanel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal21NewPromotedClassPanel10metaObjectE'
        'v',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def promotedHeaderSuffix(self) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::NewPromotedClassPanel::promotedHeaderSuffix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newpromotedclasspanel.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      qdesigner_internal::NewPromotedClassPanel::promotedHeaderSuffix()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal21NewPromotedClassPanel20promotedHea'
        'derSuffixEv',
    )

  def isPromotedHeaderLowerCase(self) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::NewPromotedClassPanel::isPromotedHeaderLowerCase()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newpromotedclasspanel.html
    """
    #  bool qdesigner_internal::NewPromotedClassPanel::
    #      isPromotedHeaderLowerCase() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal21NewPromotedClassPanel25isPromotedH'
        'eaderLowerCaseEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPromotedHeaderSuffix(self, s: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::NewPromotedClassPanel::setPromotedHeaderSuffix(const
    QString &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newpromotedclasspanel.html

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::NewPromotedClassPanel::
    #      setPromotedHeaderSuffix(const QString &s)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal21NewPromotedClassPanel23setPromotedH'
        'eaderSuffixERK7QString',
        s,
    )

  @overload(bool)
  def setPromotedHeaderLowerCase(self, l: bool) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::NewPromotedClassPanel::setPromotedHeaderLowerCase(
    bool l)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newpromotedclasspanel.html

    Parameters
    ----------

    l : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::NewPromotedClassPanel::
    #      setPromotedHeaderLowerCase(bool l)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal21NewPromotedClassPanel26setPromotedH'
        'eaderLowerCaseEb',
        l,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'qdesigner_internal::NewPromotedClassPanel::NewPromotedClassPanel(const
    QStringList &baseClasses, int selectedBaseClass, QWidget *parent)': leans
    on 'qdesigner_internal::NewPromotedClassPanel::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'qdesigner_internal.NewPromotedClassPanel.__init__' has no cute "
        "function yet. Qt's "
        "'qdesigner_internal::NewPromotedClassPanel::NewPromotedClassPanel(c"
        "onst QStringList &baseClasses, int selectedBaseClass, QWidget "
        "*parent)': leans on "
        "'qdesigner_internal::NewPromotedClassPanel::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def grabFocus(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::NewPromotedClassPanel::grabFocus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newpromotedclasspanel.html
    """
    #  void qdesigner_internal::NewPromotedClassPanel::grabFocus()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal21NewPromotedClassPanel9grabFocusEv',
    )

  @overload(str)
  def chooseBaseClass(self, a0: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::NewPromotedClassPanel::chooseBaseClass(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newpromotedclasspanel.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::NewPromotedClassPanel::chooseBaseClass(const
    #      QString &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal21NewPromotedClassPanel15chooseBaseCl'
        'assERK7QString',
        a0,
    )

  @overload(str)
  def slotNameChanged(self, a0: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::NewPromotedClassPanel::slotNameChanged(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newpromotedclasspanel.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::NewPromotedClassPanel::slotNameChanged(const
    #      QString &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal21NewPromotedClassPanel15slotNameChan'
        'gedERK7QString',
        a0,
    )

  @overload(str)
  def slotIncludeFileChanged(self, a0: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::NewPromotedClassPanel::slotIncludeFileChanged(const
    QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newpromotedclasspanel.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void
    #      qdesigner_internal::NewPromotedClassPanel::slotIncludeFileChanged(
    #      const QString &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal21NewPromotedClassPanel22slotIncludeF'
        'ileChangedERK7QString',
        a0,
    )

  def slotAdd(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::NewPromotedClassPanel::slotAdd()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newpromotedclasspanel.html
    """
    #  void qdesigner_internal::NewPromotedClassPanel::slotAdd()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal21NewPromotedClassPanel7slotAddEv',
    )

  def slotReset(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::NewPromotedClassPanel::slotReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newpromotedclasspanel.html
    """
    #  void qdesigner_internal::NewPromotedClassPanel::slotReset()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal21NewPromotedClassPanel9slotResetEv',
    )

  def enableButtons(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::NewPromotedClassPanel::enableButtons()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newpromotedclasspanel.html
    """
    #  void qdesigner_internal::NewPromotedClassPanel::enableButtons()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal21NewPromotedClassPanel13enableButton'
        'sEv',
    )

  @staticmethod
  def newPromotedClass(*__, **_) -> Never:
    """
    Qt's 'void
    qdesigner_internal::NewPromotedClassPanel::newPromotedClass(const
    PromotionParameters &a0, bool *ok)': the compiler refuses its ritual as
    it would be written here: unknown type name 'PromotionParameters'; did
    you mean 'qdesigner_internal::PromotionParameters'?.
    """
    raise NotImplementedError(
        "'qdesigner_internal.NewPromotedClassPanel.newPromotedClass' has no "
        "cute function yet. Qt's 'void "
        "qdesigner_internal::NewPromotedClassPanel::newPromotedClass(const "
        "PromotionParameters &a0, bool *ok)': the compiler refuses its "
        "ritual as it would be written here: unknown type name "
        "'PromotionParameters'; did you mean "
        "'qdesigner_internal::PromotionParameters'?.")

  @staticmethod
  def promotionParameters(*__, **_) -> Never:
    """
    Qt's 'PromotionParameters
    qdesigner_internal::NewPromotedClassPanel::promotionParameters() const':
    the compiler refuses its ritual as it would be written here: unknown type
    name 'PromotionParameters'; did you mean
    'qdesigner_internal::PromotionParameters'?.
    """
    raise NotImplementedError(
        "'qdesigner_internal.NewPromotedClassPanel.promotionParameters' has "
        "no cute function yet. Qt's 'PromotionParameters "
        "qdesigner_internal::NewPromotedClassPanel::promotionParameters() "
        "const': the compiler refuses its ritual as it would be written "
        "here: unknown type name 'PromotionParameters'; did you mean "
        "'qdesigner_internal::PromotionParameters'?.")
