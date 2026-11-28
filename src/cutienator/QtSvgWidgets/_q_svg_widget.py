"""
QSvgWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvgWidgets/qsvgwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtSvg import QtSvg
from ..QtWidgets import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QSize
  from ..QtGui import QPaintEvent
  from ..QtSvg import QSvgRenderer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QPaintEvent = WAIT['QPaintEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgWidget(QWidget):
  """
  The cute side of Qt's QSvgWidget: a plain Python object standing in front
  of one C++ QSvgWidget.

  It is built on the cute 'QWidget', as Qt's QSvgWidget is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgWidget that has a ritual and that Python can
  call so far, 8 names in all: 'metaObject', 'tr', 'renderer', 'sizeHint',
  'options', 'setOptions', 'load', 'paintEvent'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSvgWidget::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSvgWidget::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSvgWidget::~QSvgWidget()': the destructor: Python never removes a
    C++ QSvgWidget.
  - Qt's 'QSvgWidgetPrivate *QSvgWidget::d_func()': gives
    'QSvgWidgetPrivate', which has no cute class yet.
  - Qt's 'const QSvgWidgetPrivate *QSvgWidget::d_func() const': gives
    'QSvgWidgetPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QSvgWidget is created at the first use, not by 'QSvgWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgWidget.
  - Qt tells when it has removed the C++ QSvgWidget. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QSvgWidget::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgwidget.html#tr

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
    #  QString QSvgWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QSvgWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgWidget'

  #  A C++ QSvgWidget Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSvgWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSvgWidget::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QSvgWidget10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def renderer(self) -> Optional[QSvgRenderer]:
    """
    Calls Qt's 'QSvgRenderer *QSvgWidget::renderer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgwidget.html#renderer

    Returns
    -------

    Optional[QSvgRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgRenderer *QSvgWidget::renderer() const
    address = self.uglySide.call('ritual_ZNK10QSvgWidget8rendererEv')
    from ..QtSvg import QSvgRenderer
    return QSvgRenderer._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QSvgWidget::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgwidget.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSvgWidget::sizeHint() const
    ritual = 'ritual_ZNK10QSvgWidget8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSvgWidget8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def options(self) -> QtSvg.Options:
    """
    Calls Qt's 'QtSvg::Options QSvgWidget::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgwidget.html#options

    Returns
    -------

    QtSvg.Options
      The value standing for the combination Qt gave back.
    """
    #  QtSvg::Options QSvgWidget::options() const
    return QtSvg.Options(self.uglySide.call(
        'ritual_ZNK10QSvgWidget7optionsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QtSvg.Options)
  def setOptions(self, options: QtSvg.Options) -> None:
    """
    Calls Qt's 'void QSvgWidget::setOptions(QtSvg::Options options)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgwidget.html#setOptions

    Parameters
    ----------

    options : QtSvg.Options
      Passed on as its number.
    """
    #  void QSvgWidget::setOptions(QtSvg::Options options)
    self.uglySide.call(
        'ritual_ZN10QSvgWidget10setOptionsE6QFlagsIN5QtSvg6OptionEE',
        options.value,
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
    Notes what was given, for Qt's 'QSvgWidget::QSvgWidget(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgwidget.html#QSvgWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSvgWidget::QSvgWidget(QWidget *parent)
    self._noteCreation(QSvgWidget, lambda: Rituals.call(
        'ritual_ZN10QSvgWidgetC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(str)
  @overload(str, QWidget)
  @overload(str, NoneType)
  def __init__(self, file: str, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QSvgWidget::QSvgWidget(const QString
    &file, QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgwidget.html#QSvgWidget

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSvgWidget::QSvgWidget(const QString &file, QWidget *parent)
    self._noteCreation(QSvgWidget, lambda: Rituals.call(
        'ritual_ZN10QSvgWidgetC1ERK7QStringP7QWidget',
        file, self._addressOf(parent),
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
  def load(self, file: str) -> None:
    """
    Calls Qt's 'void QSvgWidget::load(const QString &file)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgwidget.html#load

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgWidget::load(const QString &file)
    self.uglySide.call('ritual_ZN10QSvgWidget4loadERK7QString', file)

  @overload(QByteArray)
  def load(self, contents: QByteArray) -> None:
    """
    Calls Qt's 'void QSvgWidget::load(const QByteArray &contents)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgwidget.html#load

    Parameters
    ----------

    contents : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSvgWidget::load(const QByteArray &contents)
    self.uglySide.call(
        'ritual_ZN10QSvgWidget4loadERK10QByteArray', self._valueOf(contents),
    )

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, event: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QSvgWidget::paintEvent(QPaintEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgwidget.html#paintEvent

    Parameters
    ----------

    event : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgWidget::paintEvent(QPaintEvent *event)
    ritual = 'ritual_ZN10QSvgWidget10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSvgWidget10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(event))
