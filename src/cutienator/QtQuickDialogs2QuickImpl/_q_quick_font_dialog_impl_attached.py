"""
QQuickFontDialogImplAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfontdialogimpl_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFontDialogImplAttached to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont
  from ..QtQuick import QQuickListView, QQuickTextEdit
  from . import QQuickFontDialogImplAttachedPrivate
  from ..QtQuickTemplates2 import QQuickCheckBox, QQuickComboBox
  from ..QtQuickTemplates2 import QQuickDialogButtonBox, QQuickTextField
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QQuickCheckBox = WAIT['QQuickCheckBox']
  QQuickComboBox = WAIT['QQuickComboBox']
  QQuickDialogButtonBox = WAIT['QQuickDialogButtonBox']
  QQuickListView = WAIT['QQuickListView']
  QQuickTextEdit = WAIT['QQuickTextEdit']
  QQuickTextField = WAIT['QQuickTextField']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFontDialogImplAttached(QObject):
  """
  The cute side of Qt's QQuickFontDialogImplAttached: a plain Python object
  standing in front of one C++ QQuickFontDialogImplAttached.

  It is built on the cute 'QObject', as Qt's QQuickFontDialogImplAttached is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFontDialogImplAttached that has a ritual and
  that Python can call so far, 50 names in all: 'metaObject', 'tr',
  'familyListView', 'setFamilyListView', 'styleListView', 'setStyleListView',
  'sizeListView', 'setSizeListView', 'sampleEdit', 'setSampleEdit',
  'buttonBox', 'setButtonBox', 'writingSystemComboBox',
  'setWritingSystemComboBox', 'underlineCheckBox', 'setUnderlineCheckBox',
  'strikeoutCheckBox', 'setStrikeoutCheckBox', 'familyEdit', 'setFamilyEdit',
  'styleEdit', 'setStyleEdit', 'sizeEdit', 'setSizeEdit', 'buttonBoxChanged',
  'familyListViewChanged', 'styleListViewChanged', 'sizeListViewChanged',
  'sampleEditChanged', 'writingSystemComboBoxChanged',
  'underlineCheckBoxChanged', 'strikeoutCheckBoxChanged',
  'familyEditChanged', 'styleEditChanged', 'sizeEditChanged', 'searchFamily',
  'searchStyle', 'clearSearch', 'updateFamilies', 'selectFontInListViews',
  'updateStyles', 'updateSizes', '_q_familyChanged', '_q_styleChanged',
  '_q_sizeEdited', '_q_sizeChanged', '_q_updateSample',
  '_q_writingSystemChanged', 'searchListView', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFontDialogImplAttached::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickFontDialogImplAttached::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickFontDialogImplAttachedPrivate
    *QQuickFontDialogImplAttached::d_func() const': takes in Python what
    'QQuickFontDialogImplAttachedPrivate
    *QQuickFontDialogImplAttached::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 58 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickFontDialogImplAttached is created at the first use, not by
    'QQuickFontDialogImplAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFontDialogImplAttached.
  - Qt tells when it has removed the C++ QQuickFontDialogImplAttached. Every
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
    Calls Qt's 'QString QQuickFontDialogImplAttached::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#tr

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
    #  QString QQuickFontDialogImplAttached::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QQuickFontDialogImplAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFontDialogImplAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFontDialogImplAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFontDialogImplAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFontDialogImplAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def familyListView(self) -> Optional[QQuickListView]:
    """
    Calls Qt's 'QQuickListView
    *QQuickFontDialogImplAttached::familyListView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#familyListView

    Returns
    -------

    Optional[QQuickListView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickListView *QQuickFontDialogImplAttached::familyListView() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFontDialogImplAttached14familyListViewEv',
    )
    from ..QtQuick import QQuickListView
    return QQuickListView._cuteAt(address)

  def styleListView(self) -> Optional[QQuickListView]:
    """
    Calls Qt's 'QQuickListView *QQuickFontDialogImplAttached::styleListView()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#styleListView

    Returns
    -------

    Optional[QQuickListView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickListView *QQuickFontDialogImplAttached::styleListView() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFontDialogImplAttached13styleListViewEv',
    )
    from ..QtQuick import QQuickListView
    return QQuickListView._cuteAt(address)

  def sizeListView(self) -> Optional[QQuickListView]:
    """
    Calls Qt's 'QQuickListView *QQuickFontDialogImplAttached::sizeListView()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#sizeListView

    Returns
    -------

    Optional[QQuickListView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickListView *QQuickFontDialogImplAttached::sizeListView() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFontDialogImplAttached12sizeListViewEv',
    )
    from ..QtQuick import QQuickListView
    return QQuickListView._cuteAt(address)

  def sampleEdit(self) -> Optional[QQuickTextEdit]:
    """
    Calls Qt's 'QQuickTextEdit *QQuickFontDialogImplAttached::sampleEdit()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#sampleEdit

    Returns
    -------

    Optional[QQuickTextEdit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextEdit *QQuickFontDialogImplAttached::sampleEdit() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFontDialogImplAttached10sampleEditEv',
    )
    from ..QtQuick import QQuickTextEdit
    return QQuickTextEdit._cuteAt(address)

  def buttonBox(self) -> Optional[QQuickDialogButtonBox]:
    """
    Calls Qt's 'QQuickDialogButtonBox
    *QQuickFontDialogImplAttached::buttonBox() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#buttonBox

    Returns
    -------

    Optional[QQuickDialogButtonBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialogButtonBox *QQuickFontDialogImplAttached::buttonBox() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFontDialogImplAttached9buttonBoxEv',
    )
    from ..QtQuickTemplates2 import QQuickDialogButtonBox
    return QQuickDialogButtonBox._cuteAt(address)

  def writingSystemComboBox(self) -> Optional[QQuickComboBox]:
    """
    Calls Qt's 'QQuickComboBox
    *QQuickFontDialogImplAttached::writingSystemComboBox() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html

    Returns
    -------

    Optional[QQuickComboBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickComboBox *QQuickFontDialogImplAttached::writingSystemComboBox()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFontDialogImplAttached21writingSystemComboBoxEv',
    )
    from ..QtQuickTemplates2 import QQuickComboBox
    return QQuickComboBox._cuteAt(address)

  def underlineCheckBox(self) -> Optional[QQuickCheckBox]:
    """
    Calls Qt's 'QQuickCheckBox
    *QQuickFontDialogImplAttached::underlineCheckBox() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html

    Returns
    -------

    Optional[QQuickCheckBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickCheckBox *QQuickFontDialogImplAttached::underlineCheckBox()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFontDialogImplAttached17underlineCheckBoxEv',
    )
    from ..QtQuickTemplates2 import QQuickCheckBox
    return QQuickCheckBox._cuteAt(address)

  def strikeoutCheckBox(self) -> Optional[QQuickCheckBox]:
    """
    Calls Qt's 'QQuickCheckBox
    *QQuickFontDialogImplAttached::strikeoutCheckBox() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html

    Returns
    -------

    Optional[QQuickCheckBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickCheckBox *QQuickFontDialogImplAttached::strikeoutCheckBox()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFontDialogImplAttached17strikeoutCheckBoxEv',
    )
    from ..QtQuickTemplates2 import QQuickCheckBox
    return QQuickCheckBox._cuteAt(address)

  def familyEdit(self) -> Optional[QQuickTextField]:
    """
    Calls Qt's 'QQuickTextField *QQuickFontDialogImplAttached::familyEdit()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#familyEdit

    Returns
    -------

    Optional[QQuickTextField]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextField *QQuickFontDialogImplAttached::familyEdit() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFontDialogImplAttached10familyEditEv',
    )
    from ..QtQuickTemplates2 import QQuickTextField
    return QQuickTextField._cuteAt(address)

  def styleEdit(self) -> Optional[QQuickTextField]:
    """
    Calls Qt's 'QQuickTextField *QQuickFontDialogImplAttached::styleEdit()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#styleEdit

    Returns
    -------

    Optional[QQuickTextField]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextField *QQuickFontDialogImplAttached::styleEdit() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFontDialogImplAttached9styleEditEv',
    )
    from ..QtQuickTemplates2 import QQuickTextField
    return QQuickTextField._cuteAt(address)

  def sizeEdit(self) -> Optional[QQuickTextField]:
    """
    Calls Qt's 'QQuickTextField *QQuickFontDialogImplAttached::sizeEdit()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#sizeEdit

    Returns
    -------

    Optional[QQuickTextField]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextField *QQuickFontDialogImplAttached::sizeEdit() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFontDialogImplAttached8sizeEditEv',
    )
    from ..QtQuickTemplates2 import QQuickTextField
    return QQuickTextField._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickListView)
  @overload(NoneType)
  def setFamilyListView(
      self,
      familyListView: Optional[QQuickListView],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplAttached::setFamilyListView(QQuickListView
    *familyListView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html

    Parameters
    ----------

    familyListView : Optional[QQuickListView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFontDialogImplAttached::setFamilyListView(QQuickListView
    #      *familyListView)
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached17setFamilyListViewEP14QQui'
        'ckListView',
        self._addressOf(familyListView),
    )

  @overload(QQuickListView)
  @overload(NoneType)
  def setStyleListView(
      self,
      styleListView: Optional[QQuickListView],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplAttached::setStyleListView(QQuickListView
    *styleListView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#setStyleListView

    Parameters
    ----------

    styleListView : Optional[QQuickListView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFontDialogImplAttached::setStyleListView(QQuickListView
    #      *styleListView)
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached16setStyleListViewEP14QQuic'
        'kListView',
        self._addressOf(styleListView),
    )

  @overload(QQuickListView)
  @overload(NoneType)
  def setSizeListView(self, sizeListView: Optional[QQuickListView]) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplAttached::setSizeListView(QQuickListView
    *sizeListView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#setSizeListView

    Parameters
    ----------

    sizeListView : Optional[QQuickListView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFontDialogImplAttached::setSizeListView(QQuickListView
    #      *sizeListView)
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached15setSizeListViewEP14QQuick'
        'ListView',
        self._addressOf(sizeListView),
    )

  @overload(QQuickTextEdit)
  @overload(NoneType)
  def setSampleEdit(self, sampleEdit: Optional[QQuickTextEdit]) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplAttached::setSampleEdit(QQuickTextEdit *sampleEdit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#setSampleEdit

    Parameters
    ----------

    sampleEdit : Optional[QQuickTextEdit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFontDialogImplAttached::setSampleEdit(QQuickTextEdit
    #      *sampleEdit)
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached13setSampleEditEP14QQuickTe'
        'xtEdit',
        self._addressOf(sampleEdit),
    )

  @overload(QQuickDialogButtonBox)
  @overload(NoneType)
  def setButtonBox(self, buttonBox: Optional[QQuickDialogButtonBox]) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplAttached::setButtonBox(QQuickDialogButtonBox
    *buttonBox)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#setButtonBox

    Parameters
    ----------

    buttonBox : Optional[QQuickDialogButtonBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFontDialogImplAttached::setButtonBox(QQuickDialogButtonBox
    #      *buttonBox)
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached12setButtonBoxEP21QQuickDia'
        'logButtonBox',
        self._addressOf(buttonBox),
    )

  @overload(QQuickComboBox)
  @overload(NoneType)
  def setWritingSystemComboBox(
      self,
      writingSystemComboBox: Optional[QQuickComboBox],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplAttached::setWritingSystemComboBox(QQuickComboBox
    *writingSystemComboBox)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html

    Parameters
    ----------

    writingSystemComboBox : Optional[QQuickComboBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFontDialogImplAttached::setWritingSystemComboBox(
    #      QQuickComboBox *writingSystemComboBox)
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached24setWritingSystemComboBoxE'
        'P14QQuickComboBox',
        self._addressOf(writingSystemComboBox),
    )

  @overload(QQuickCheckBox)
  @overload(NoneType)
  def setUnderlineCheckBox(
      self,
      underlineCheckBox: Optional[QQuickCheckBox],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplAttached::setUnderlineCheckBox(QQuickCheckBox
    *underlineCheckBox)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html

    Parameters
    ----------

    underlineCheckBox : Optional[QQuickCheckBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFontDialogImplAttached::setUnderlineCheckBox(QQuickCheckBox
    #      *underlineCheckBox)
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached20setUnderlineCheckBoxEP14Q'
        'QuickCheckBox',
        self._addressOf(underlineCheckBox),
    )

  @overload(QQuickCheckBox)
  @overload(NoneType)
  def setStrikeoutCheckBox(
      self,
      strikethroughCheckBox: Optional[QQuickCheckBox],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplAttached::setStrikeoutCheckBox(QQuickCheckBox
    *strikethroughCheckBox)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html

    Parameters
    ----------

    strikethroughCheckBox : Optional[QQuickCheckBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFontDialogImplAttached::setStrikeoutCheckBox(QQuickCheckBox
    #      *strikethroughCheckBox)
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached20setStrikeoutCheckBoxEP14Q'
        'QuickCheckBox',
        self._addressOf(strikethroughCheckBox),
    )

  @overload(QQuickTextField)
  @overload(NoneType)
  def setFamilyEdit(self, familyEdit: Optional[QQuickTextField]) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplAttached::setFamilyEdit(QQuickTextField
    *familyEdit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#setFamilyEdit

    Parameters
    ----------

    familyEdit : Optional[QQuickTextField]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFontDialogImplAttached::setFamilyEdit(QQuickTextField
    #      *familyEdit)
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached13setFamilyEditEP15QQuickTe'
        'xtField',
        self._addressOf(familyEdit),
    )

  @overload(QQuickTextField)
  @overload(NoneType)
  def setStyleEdit(self, styleEdit: Optional[QQuickTextField]) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplAttached::setStyleEdit(QQuickTextField *styleEdit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#setStyleEdit

    Parameters
    ----------

    styleEdit : Optional[QQuickTextField]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFontDialogImplAttached::setStyleEdit(QQuickTextField
    #      *styleEdit)
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached12setStyleEditEP15QQuickTex'
        'tField',
        self._addressOf(styleEdit),
    )

  @overload(QQuickTextField)
  @overload(NoneType)
  def setSizeEdit(self, sizeEdit: Optional[QQuickTextField]) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplAttached::setSizeEdit(QQuickTextField *sizeEdit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#setSizeEdit

    Parameters
    ----------

    sizeEdit : Optional[QQuickTextField]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFontDialogImplAttached::setSizeEdit(QQuickTextField
    #      *sizeEdit)
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached11setSizeEditEP15QQuickText'
        'Field',
        self._addressOf(sizeEdit),
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
    'QQuickFontDialogImplAttached::QQuickFontDialogImplAttached(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFontDialogImplAttached::QQuickFontDialogImplAttached(QObject
    #      *parent)
    self._noteCreation(QQuickFontDialogImplAttached, lambda: Rituals.call(
        'ritual_ZN28QQuickFontDialogImplAttachedC1EP7QObject',
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
    Calls Qt's 'void QQuickFontDialogImplAttached::buttonBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#buttonBoxChanged
    """
    #  void QQuickFontDialogImplAttached::buttonBoxChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached16buttonBoxChangedEv',
    )

  def familyListViewChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::familyListViewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html
    """
    #  void QQuickFontDialogImplAttached::familyListViewChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached21familyListViewChangedEv',
    )

  def styleListViewChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::styleListViewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html
    """
    #  void QQuickFontDialogImplAttached::styleListViewChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached20styleListViewChangedEv',
    )

  def sizeListViewChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::sizeListViewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html
    """
    #  void QQuickFontDialogImplAttached::sizeListViewChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached19sizeListViewChangedEv',
    )

  def sampleEditChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::sampleEditChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html
    """
    #  void QQuickFontDialogImplAttached::sampleEditChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached17sampleEditChangedEv',
    )

  def writingSystemComboBoxChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplAttached::writingSystemComboBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html
    """
    #  void QQuickFontDialogImplAttached::writingSystemComboBoxChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached28writingSystemComboBoxChan'
        'gedEv',
    )

  def underlineCheckBoxChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplAttached::underlineCheckBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html
    """
    #  void QQuickFontDialogImplAttached::underlineCheckBoxChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached24underlineCheckBoxChangedE'
        'v',
    )

  def strikeoutCheckBoxChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplAttached::strikeoutCheckBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html
    """
    #  void QQuickFontDialogImplAttached::strikeoutCheckBoxChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached24strikeoutCheckBoxChangedE'
        'v',
    )

  def familyEditChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::familyEditChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html
    """
    #  void QQuickFontDialogImplAttached::familyEditChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached17familyEditChangedEv',
    )

  def styleEditChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::styleEditChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#styleEditChanged
    """
    #  void QQuickFontDialogImplAttached::styleEditChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached16styleEditChangedEv',
    )

  def sizeEditChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::sizeEditChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#sizeEditChanged
    """
    #  void QQuickFontDialogImplAttached::sizeEditChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached15sizeEditChangedEv',
    )

  @overload(str)
  def searchFamily(self, s: str) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::searchFamily(const QString
    &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#searchFamily

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFontDialogImplAttached::searchFamily(const QString &s)
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached12searchFamilyERK7QString',
        s,
    )

  @overload(str)
  def searchStyle(self, s: str) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::searchStyle(const QString
    &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#searchStyle

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFontDialogImplAttached::searchStyle(const QString &s)
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached11searchStyleERK7QString', s,
    )

  def clearSearch(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::clearSearch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#clearSearch
    """
    #  void QQuickFontDialogImplAttached::clearSearch()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached11clearSearchEv',
    )

  def updateFamilies(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::updateFamilies()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#updateFamilies
    """
    #  void QQuickFontDialogImplAttached::updateFamilies()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached14updateFamiliesEv',
    )

  @overload(QFont)
  def selectFontInListViews(self, font: QFont) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplAttached::selectFontInListViews(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickFontDialogImplAttached::selectFontInListViews(const QFont
    #      &font)
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached21selectFontInListViewsERK5'
        'QFont',
        self._valueOf(font),
    )

  def updateStyles(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::updateStyles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#updateStyles
    """
    #  void QQuickFontDialogImplAttached::updateStyles()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached12updateStylesEv',
    )

  def updateSizes(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::updateSizes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#updateSizes
    """
    #  void QQuickFontDialogImplAttached::updateSizes()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached11updateSizesEv',
    )

  def _q_familyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::_q_familyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#_q_familyChanged
    """
    #  void QQuickFontDialogImplAttached::_q_familyChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached16_q_familyChangedEv',
    )

  def _q_styleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::_q_styleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#_q_styleChanged
    """
    #  void QQuickFontDialogImplAttached::_q_styleChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached15_q_styleChangedEv',
    )

  def _q_sizeEdited(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::_q_sizeEdited()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#_q_sizeEdited
    """
    #  void QQuickFontDialogImplAttached::_q_sizeEdited()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached13_q_sizeEditedEv',
    )

  def _q_sizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::_q_sizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#_q_sizeChanged
    """
    #  void QQuickFontDialogImplAttached::_q_sizeChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached14_q_sizeChangedEv',
    )

  def _q_updateSample(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::_q_updateSample()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#_q_updateSample
    """
    #  void QQuickFontDialogImplAttached::_q_updateSample()
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached15_q_updateSampleEv',
    )

  @overload(int)
  def _q_writingSystemChanged(self, index: int) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialogImplAttached::_q_writingSystemChanged(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuickFontDialogImplAttached::_q_writingSystemChanged(int index)
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached23_q_writingSystemChangedEi',
        index,
    )

  @overload(str, QQuickListView)
  @overload(str, NoneType)
  def searchListView(
      self,
      s: str,
      listView: Optional[QQuickListView],
  ) -> None:
    """
    Calls Qt's 'void QQuickFontDialogImplAttached::searchListView(const
    QString &s, QQuickListView *listView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#searchListView

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    listView : Optional[QQuickListView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFontDialogImplAttached::searchListView(const QString &s,
    #      QQuickListView *listView)
    self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached14searchListViewERK7QString'
        'P14QQuickListView',
        s, self._addressOf(listView),
    )

  def d_func(self) -> Optional[QQuickFontDialogImplAttachedPrivate]:
    """
    Calls Qt's 'QQuickFontDialogImplAttachedPrivate
    *QQuickFontDialogImplAttached::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialogimplattached.html#d_func

    Returns
    -------

    Optional[QQuickFontDialogImplAttachedPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFontDialogImplAttachedPrivate
    #      *QQuickFontDialogImplAttached::d_func()
    address = self.uglySide.call(
        'ritual_ZN28QQuickFontDialogImplAttached6d_funcEv',
    )
    from . import QQuickFontDialogImplAttachedPrivate
    return QQuickFontDialogImplAttachedPrivate._cuteAt(address)
