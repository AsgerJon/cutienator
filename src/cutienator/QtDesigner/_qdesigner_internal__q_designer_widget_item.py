"""
qdesigner_internal::QDesignerWidgetItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_widgetitem_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::QDesignerWidgetItem to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtWidgets import QWidgetItemV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QSize
  from ..QtWidgets import QLayout, QWidget
  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QEvent = WAIT['QEvent']
  QLayout = WAIT['QLayout']
  QSize = WAIT['QSize']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerWidgetItem(QObject, QWidgetItemV2):
  """
  The cute side of Qt's qdesigner_internal::QDesignerWidgetItem: a plain
  Python object standing in front of one C++
  qdesigner_internal::QDesignerWidgetItem.

  It is built on the cute 'QObject', as Qt's
  qdesigner_internal::QDesignerWidgetItem is built on Qt's QObject, and has
  everything that class has. It is built on the cute 'QWidgetItemV2' as well,
  as Qt's qdesigner_internal::QDesignerWidgetItem is built on Qt's
  QWidgetItemV2 too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::QDesignerWidgetItem that has a
  ritual and that Python can call so far, 17 names in all: 'metaObject',
  'tr', 'containingLayout', 'constWidget', 'minimumSize', 'sizeHint',
  'nonLaidOutMinSize', 'setNonLaidOutMinSize', 'nonLaidOutSizeHint',
  'setNonLaidOutSizeHint', 'install', 'deinstall', 'isContainer',
  'subjectToStretch', 'eventFilter', 'layoutChanged', 'expand'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::QDesignerWidgetItem::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::QDesignerWidgetItem::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'bool qdesigner_internal::QDesignerWidgetItem::check(const QLayout
    *layout, QWidget *w, Qt::Orientations *ptrToOrientations)': names
    'Qt::Orientations', which has no cute class yet.

  What has no ritual
  ------------------

  6 of the 28 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::QDesignerWidgetItem is created at the first
    use, not by 'qdesigner_internal::QDesignerWidgetItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::QDesignerWidgetItem.
  - Qt tells when it has removed the C++
    qdesigner_internal::QDesignerWidgetItem. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  - Each name of Qt's qdesigner_internal::QDesignerWidgetItem that has no
    cute function yet, 'check', holds a function that raises
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
    Calls Qt's 'QString qdesigner_internal::QDesignerWidgetItem::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html#tr

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
    #  QString qdesigner_internal::QDesignerWidgetItem::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal19QDesignerWidgetItem2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def install() -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerWidgetItem::install()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html
    """
    #  void qdesigner_internal::QDesignerWidgetItem::install()
    Rituals.call(
        'ritual_ZN18qdesigner_internal19QDesignerWidgetItem7installEv',
    )

  @staticmethod
  def deinstall() -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerWidgetItem::deinstall()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html
    """
    #  void qdesigner_internal::QDesignerWidgetItem::deinstall()
    Rituals.call(
        'ritual_ZN18qdesigner_internal19QDesignerWidgetItem9deinstallEv',
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def isContainer(
      core: Optional[QDesignerFormEditorInterface],
      w: Optional[QWidget],
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QDesignerWidgetItem::isContainer(const
    QDesignerFormEditorInterface *core, QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::QDesignerWidgetItem::isContainer(const
    #      QDesignerFormEditorInterface *core, QWidget *w)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal19QDesignerWidgetItem11isContainerEPK'
        '28QDesignerFormEditorInterfaceP7QWidget',
        CuteMixin._addressOf(core), CuteMixin._addressOf(w),
    )

  @staticmethod
  @overload(QLayout, QWidget)
  @overload(QLayout, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def subjectToStretch(
      layout: Optional[QLayout],
      w: Optional[QWidget],
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QDesignerWidgetItem::subjectToStretch(const QLayout
    *layout, QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html

    Parameters
    ----------

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::QDesignerWidgetItem::subjectToStretch(const
    #      QLayout *layout, QWidget *w)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal19QDesignerWidgetItem16subjectToStret'
        'chEPK7QLayoutP7QWidget',
        CuteMixin._addressOf(layout), CuteMixin._addressOf(w),
    )

  @overload()
  def subjectToStretch(self) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QDesignerWidgetItem::subjectToStretch() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html
    """
    #  bool qdesigner_internal::QDesignerWidgetItem::subjectToStretch() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal19QDesignerWidgetItem16subjectToStre'
        'tchEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::QDesignerWidgetItem'

  #  Qt's qdesigner_internal::QDesignerWidgetItem is built on more than one
  #  class. The part of a C++ qdesigner_internal::QDesignerWidgetItem that
  #  belongs to a class after the first begins somewhere inside the object,
  #  and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QWidgetItemV2':
          'ritual_cast_qdesigner_internal_QDesignerWidgetItem_QWidgetItemV2',
  }

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
    *qdesigner_internal::QDesignerWidgetItem::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *qdesigner_internal::QDesignerWidgetItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal19QDesignerWidgetItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def containingLayout(self) -> Optional[QLayout]:
    """
    Calls Qt's 'const QLayout
    *qdesigner_internal::QDesignerWidgetItem::containingLayout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QLayout
    #      *qdesigner_internal::QDesignerWidgetItem::containingLayout() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal19QDesignerWidgetItem16containingLay'
        'outEv',
    )
    from ..QtWidgets import QLayout
    return QLayout._cuteAt(address)

  def constWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::QDesignerWidgetItem::constWidget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::QDesignerWidgetItem::constWidget() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal19QDesignerWidgetItem11constWidgetEv',
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize qdesigner_internal::QDesignerWidgetItem::minimumSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize qdesigner_internal::QDesignerWidgetItem::minimumSize() const
    ritual = (
        'ritual_ZNK18qdesigner_internal19QDesignerWidgetItem11minimumSizeEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal19QDesignerWidgetItem11minimum'
          'SizeEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize qdesigner_internal::QDesignerWidgetItem::sizeHint()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize qdesigner_internal::QDesignerWidgetItem::sizeHint() const
    ritual = 'ritual_ZNK18qdesigner_internal19QDesignerWidgetItem8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal19QDesignerWidgetItem8sizeHint'
          'Ev')
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def nonLaidOutMinSize(self) -> QSize:
    """
    Calls Qt's 'QSize
    qdesigner_internal::QDesignerWidgetItem::nonLaidOutMinSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize qdesigner_internal::QDesignerWidgetItem::nonLaidOutMinSize()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal19QDesignerWidgetItem17nonLaidOutMin'
        'SizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def nonLaidOutSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize
    qdesigner_internal::QDesignerWidgetItem::nonLaidOutSizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize qdesigner_internal::QDesignerWidgetItem::nonLaidOutSizeHint()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal19QDesignerWidgetItem18nonLaidOutSiz'
        'eHintEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def setNonLaidOutMinSize(self, s: QSize) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerWidgetItem::setNonLaidOutMinSize(const QSize
    &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void qdesigner_internal::QDesignerWidgetItem::setNonLaidOutMinSize(
    #      const QSize &s)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal19QDesignerWidgetItem20setNonLaidOutM'
        'inSizeERK5QSize',
        self._valueOf(s),
    )

  @overload(QSize)
  def setNonLaidOutSizeHint(self, s: QSize) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerWidgetItem::setNonLaidOutSizeHint(const
    QSize &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void qdesigner_internal::QDesignerWidgetItem::setNonLaidOutSizeHint(
    #      const QSize &s)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal19QDesignerWidgetItem21setNonLaidOutS'
        'izeHintERK5QSize',
        self._valueOf(s),
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

  @overload(QLayout, QWidget)
  @overload(QLayout, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  @overload(QLayout, QWidget, Qt.Orientations)
  @overload(QLayout, NoneType, Qt.Orientations)
  @overload(NoneType, QWidget, Qt.Orientations)
  @overload(NoneType, NoneType, Qt.Orientations)
  def __init__(
      self,
      containingLayout: Optional[QLayout],
      w: Optional[QWidget],
      o: Qt.Orientations = (
          Qt.Orientations.Horizontal | Qt.Orientations.Vertical),
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::QDesignerWidgetItem::QDesignerWidgetItem(const
    QLayout *containingLayout, QWidget *w, Qt::Orientations o)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html

    Parameters
    ----------

    containingLayout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    o : Qt.Orientations
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientations.Horizontal | Qt.Orientations.Vertical.
    """
    #  qdesigner_internal::QDesignerWidgetItem::QDesignerWidgetItem(const
    #      QLayout *containingLayout, QWidget *w, Qt::Orientations o)
    self._noteCreation(QDesignerWidgetItem, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal19QDesignerWidgetItemC1EPK7QLayoutP7Q'
        'Widget6QFlagsIN2Qt11OrientationEE',
        self._addressOf(containingLayout), self._addressOf(w), o.value,
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

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      watched: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QDesignerWidgetItem::eventFilter(QObject *watched,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html

    Parameters
    ----------

    watched : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::QDesignerWidgetItem::eventFilter(QObject
    #      *watched, QEvent *event)
    ritual = (
        'ritual_ZN18qdesigner_internal19QDesignerWidgetItem11eventFilterEP7'
        'QObjectP6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal19QDesignerWidgetItem11eventFil'
          'terEP7QObjectP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(watched, 'QObject'), self._addressOf(event),
    )

  def layoutChanged(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerWidgetItem::layoutChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html
    """
    #  void qdesigner_internal::QDesignerWidgetItem::layoutChanged()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal19QDesignerWidgetItem13layoutChangedE'
        'v',
    )

  @overload(QSize)
  @overload(NoneType)
  def expand(self, s: Optional[QSize]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerWidgetItem::expand(QSize
    *s) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetitem.html#expand

    Parameters
    ----------

    s : Optional[QSize]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::QDesignerWidgetItem::expand(QSize *s) const
    self.uglySide.call(
        'ritual_ZNK18qdesigner_internal19QDesignerWidgetItem6expandEP5QSize',
        self._addressOf(s),
    )

  @staticmethod
  def check(*__, **_) -> Never:
    """
    Qt's 'bool qdesigner_internal::QDesignerWidgetItem::check(const QLayout
    *layout, QWidget *w, Qt::Orientations *ptrToOrientations)': names
    'Qt::Orientations', which has no cute class yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QDesignerWidgetItem.check' has no cute "
        "function yet. Qt's 'bool "
        "qdesigner_internal::QDesignerWidgetItem::check(const QLayout "
        "*layout, QWidget *w, Qt::Orientations *ptrToOrientations)': names "
        "'Qt::Orientations', which has no cute class yet.")
