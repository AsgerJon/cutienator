"""
QAbstractScrollArea binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qabstractscrollarea.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QAbstractScrollAreaSizeAdjustPolicy, QFrame, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize
  from . import QScrollBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScrollBar = WAIT['QScrollBar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractScrollArea(QFrame):
  """
  The cute side of Qt's QAbstractScrollArea: a plain Python object standing
  in front of one C++ QAbstractScrollArea.

  It is built on the cute 'QFrame', as Qt's QAbstractScrollArea is built on
  Qt's QFrame, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractScrollArea that has a ritual and that
  Python can call so far, 21 names in all: 'metaObject', 'tr',
  'verticalScrollBarPolicy', 'setVerticalScrollBarPolicy',
  'verticalScrollBar', 'setVerticalScrollBar', 'horizontalScrollBarPolicy',
  'setHorizontalScrollBarPolicy', 'horizontalScrollBar',
  'setHorizontalScrollBar', 'cornerWidget', 'setCornerWidget',
  'addScrollBarWidget', 'viewport', 'setViewport', 'maximumViewportSize',
  'minimumSizeHint', 'sizeHint', 'setupViewport', 'sizeAdjustPolicy',
  'setSizeAdjustPolicy'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractScrollArea::~QAbstractScrollArea()': the destructor:
    Python never removes a C++ QAbstractScrollArea.

  What has no ritual
  ------------------

  31 of the 54 functions Qt declares: 22 protected; 3 takes or gives a type
  that cannot be passed yet; 3 private; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QAbstractScrollArea is created at the first use, not by
    'QAbstractScrollArea(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractScrollArea.
  - Qt tells when it has removed the C++ QAbstractScrollArea. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QAbstractScrollArea, and the names Qt has for
  #  the combinations of its flags enums.
  SizeAdjustPolicy = QAbstractScrollAreaSizeAdjustPolicy

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
    Calls Qt's 'QString QAbstractScrollArea::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractscrollarea.html#tr

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
    #  QString QAbstractScrollArea::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QAbstractScrollArea2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractScrollArea'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractScrollArea::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractScrollArea::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def verticalScrollBarPolicy(self) -> Qt.ScrollBarPolicy:
    """
    Calls Qt's 'Qt::ScrollBarPolicy
    QAbstractScrollArea::verticalScrollBarPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#verticalScrollBarPolicy

    Returns
    -------

    Qt.ScrollBarPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ScrollBarPolicy(number)' gives.
    """
    #  Qt::ScrollBarPolicy QAbstractScrollArea::verticalScrollBarPolicy()
    #      const
    return Qt.ScrollBarPolicy(self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea23verticalScrollBarPolicyEv',
    ))

  def verticalScrollBar(self) -> Optional[QScrollBar]:
    """
    Calls Qt's 'QScrollBar *QAbstractScrollArea::verticalScrollBar() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#verticalScrollBar

    Returns
    -------

    Optional[QScrollBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScrollBar *QAbstractScrollArea::verticalScrollBar() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea17verticalScrollBarEv',
    )
    from . import QScrollBar
    return QScrollBar._cuteAt(address)

  def horizontalScrollBarPolicy(self) -> Qt.ScrollBarPolicy:
    """
    Calls Qt's 'Qt::ScrollBarPolicy
    QAbstractScrollArea::horizontalScrollBarPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#horizontalScrollBarPolicy

    Returns
    -------

    Qt.ScrollBarPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ScrollBarPolicy(number)' gives.
    """
    #  Qt::ScrollBarPolicy QAbstractScrollArea::horizontalScrollBarPolicy()
    #      const
    return Qt.ScrollBarPolicy(self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea25horizontalScrollBarPolicyEv',
    ))

  def horizontalScrollBar(self) -> Optional[QScrollBar]:
    """
    Calls Qt's 'QScrollBar *QAbstractScrollArea::horizontalScrollBar()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#horizontalScrollBar

    Returns
    -------

    Optional[QScrollBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScrollBar *QAbstractScrollArea::horizontalScrollBar() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea19horizontalScrollBarEv',
    )
    from . import QScrollBar
    return QScrollBar._cuteAt(address)

  def cornerWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QAbstractScrollArea::cornerWidget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#cornerWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QAbstractScrollArea::cornerWidget() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea12cornerWidgetEv',
    )
    return QWidget._cuteAt(address)

  def viewport(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QAbstractScrollArea::viewport() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractscrollarea.html#viewport

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QAbstractScrollArea::viewport() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea8viewportEv',
    )
    return QWidget._cuteAt(address)

  def maximumViewportSize(self) -> QSize:
    """
    Calls Qt's 'QSize QAbstractScrollArea::maximumViewportSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#maximumViewportSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAbstractScrollArea::maximumViewportSize() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea19maximumViewportSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QAbstractScrollArea::minimumSizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAbstractScrollArea::minimumSizeHint() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea15minimumSizeHintEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QAbstractScrollArea::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractscrollarea.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAbstractScrollArea::sizeHint() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea8sizeHintEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizeAdjustPolicy(self) -> SizeAdjustPolicy:
    """
    Calls Qt's 'SizeAdjustPolicy QAbstractScrollArea::sizeAdjustPolicy()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#sizeAdjustPolicy

    Returns
    -------

    SizeAdjustPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SizeAdjustPolicy(number)'
      gives.
    """
    #  SizeAdjustPolicy QAbstractScrollArea::sizeAdjustPolicy() const
    return QAbstractScrollArea.SizeAdjustPolicy(self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea16sizeAdjustPolicyEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.ScrollBarPolicy)
  def setVerticalScrollBarPolicy(self, a0: Qt.ScrollBarPolicy) -> None:
    """
    Calls Qt's 'void
    QAbstractScrollArea::setVerticalScrollBarPolicy(Qt::ScrollBarPolicy a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html

    Parameters
    ----------

    a0 : Qt.ScrollBarPolicy
      Passed on as its number.
    """
    #  void QAbstractScrollArea::setVerticalScrollBarPolicy(Qt::
    #      ScrollBarPolicy a0)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea26setVerticalScrollBarPolicyEN2Qt15S'
        'crollBarPolicyE',
        a0.value,
    )

  @overload(QScrollBar)
  @overload(NoneType)
  def setVerticalScrollBar(self, scrollbar: Optional[QScrollBar]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::setVerticalScrollBar(QScrollBar
    *scrollbar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#setVerticalScrollBar

    Parameters
    ----------

    scrollbar : Optional[QScrollBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::setVerticalScrollBar(QScrollBar *scrollbar)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea20setVerticalScrollBarEP10QScrollBar',
        self._addressOf(scrollbar),
    )

  @overload(Qt.ScrollBarPolicy)
  def setHorizontalScrollBarPolicy(self, a0: Qt.ScrollBarPolicy) -> None:
    """
    Calls Qt's 'void
    QAbstractScrollArea::setHorizontalScrollBarPolicy(Qt::ScrollBarPolicy
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html

    Parameters
    ----------

    a0 : Qt.ScrollBarPolicy
      Passed on as its number.
    """
    #  void QAbstractScrollArea::setHorizontalScrollBarPolicy(Qt::
    #      ScrollBarPolicy a0)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea28setHorizontalScrollBarPolicyEN2Qt1'
        '5ScrollBarPolicyE',
        a0.value,
    )

  @overload(QScrollBar)
  @overload(NoneType)
  def setHorizontalScrollBar(self, scrollbar: Optional[QScrollBar]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::setHorizontalScrollBar(QScrollBar
    *scrollbar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#setHorizontalScrollBar

    Parameters
    ----------

    scrollbar : Optional[QScrollBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::setHorizontalScrollBar(QScrollBar
    #      *scrollbar)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea22setHorizontalScrollBarEP10QScrollB'
        'ar',
        self._addressOf(scrollbar),
    )

  @overload(QWidget)
  @overload(NoneType)
  def setCornerWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::setCornerWidget(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#setCornerWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::setCornerWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea15setCornerWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QWidget)
  @overload(NoneType)
  def setViewport(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::setViewport(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#setViewport

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::setViewport(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea11setViewportEP7QWidget',
        self._addressOf(widget),
    )

  @overload(SizeAdjustPolicy)
  def setSizeAdjustPolicy(self, policy: SizeAdjustPolicy) -> None:
    """
    Calls Qt's 'void
    QAbstractScrollArea::setSizeAdjustPolicy(SizeAdjustPolicy policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#setSizeAdjustPolicy

    Parameters
    ----------

    policy : SizeAdjustPolicy
      Passed on as its number.
    """
    #  void QAbstractScrollArea::setSizeAdjustPolicy(SizeAdjustPolicy policy)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea19setSizeAdjustPolicyENS_16SizeAdjus'
        'tPolicyE',
        policy.value,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractScrollArea::QAbstractScrollArea(QWidget *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#QAbstractScrollArea

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstractScrollArea::QAbstractScrollArea(QWidget *parent)
    self._noteCreation(QAbstractScrollArea, lambda: Rituals.call(
        'ritual_ZN19QAbstractScrollAreaC1EP7QWidget',
        self._addressOf(parent),
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

  @overload(QWidget, Qt.Alignment)
  @overload(NoneType, Qt.Alignment)
  def addScrollBarWidget(
      self,
      widget: Optional[QWidget],
      alignment: Qt.Alignment,
  ) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::addScrollBarWidget(QWidget *widget,
    Qt::Alignment alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#addScrollBarWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QAbstractScrollArea::addScrollBarWidget(QWidget *widget,
    #      Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea18addScrollBarWidgetEP7QWidget6QFlag'
        'sIN2Qt13AlignmentFlagEE',
        self._addressOf(widget), alignment.value,
    )

  @overload(QWidget)
  @overload(NoneType)
  def setupViewport(self, viewport: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::setupViewport(QWidget *viewport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#setupViewport

    Parameters
    ----------

    viewport : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::setupViewport(QWidget *viewport)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea13setupViewportEP7QWidget',
        self._addressOf(viewport),
    )
