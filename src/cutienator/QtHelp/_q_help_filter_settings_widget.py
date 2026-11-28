"""
QHelpFilterSettingsWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/qhelpfiltersettingswidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from ..QtWidgets import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVersionNumber
  from . import QHelpFilterEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHelpFilterEngine = WAIT['QHelpFilterEngine']
  QVersionNumber = WAIT['QVersionNumber']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHelpFilterSettingsWidget(QWidget):
  """
  The cute side of Qt's QHelpFilterSettingsWidget: a plain Python object
  standing in front of one C++ QHelpFilterSettingsWidget.

  It is built on the cute 'QWidget', as Qt's QHelpFilterSettingsWidget is
  built on Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHelpFilterSettingsWidget that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr',
  'setAvailableComponents', 'setAvailableVersions', 'readSettings',
  'applySettings'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHelpFilterSettingsWidget::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QHelpFilterSettingsWidget::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QHelpFilterSettingsWidget::~QHelpFilterSettingsWidget()': the
    destructor: Python never removes a C++ QHelpFilterSettingsWidget.
  - Qt's 'QHelpFilterSettingsWidgetPrivate
    *QHelpFilterSettingsWidget::d_func()': gives
    'QHelpFilterSettingsWidgetPrivate', which has no cute class yet.
  - Qt's 'const QHelpFilterSettingsWidgetPrivate
    *QHelpFilterSettingsWidget::d_func() const': gives
    'QHelpFilterSettingsWidgetPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  6 of the 18 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QHelpFilterSettingsWidget is created at the first use, not by
    'QHelpFilterSettingsWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHelpFilterSettingsWidget.
  - Qt tells when it has removed the C++ QHelpFilterSettingsWidget. Every
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
    Calls Qt's 'QString QHelpFilterSettingsWidget::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpfiltersettingswidget.html#tr

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
    #  QString QHelpFilterSettingsWidget::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QHelpFilterSettingsWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHelpFilterSettingsWidget'

  #  A C++ QHelpFilterSettingsWidget Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHelpFilterSettingsWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHelpFilterSettingsWidget::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfiltersettingswidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHelpFilterSettingsWidget::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QHelpFilterSettingsWidget10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QHelpFilterEngine)
  @overload(NoneType)
  def applySettings(self, filterEngine: Optional[QHelpFilterEngine]) -> bool:
    """
    Calls Qt's 'bool
    QHelpFilterSettingsWidget::applySettings(QHelpFilterEngine *filterEngine)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfiltersettingswidget.html#applySettings

    Parameters
    ----------

    filterEngine : Optional[QHelpFilterEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QHelpFilterSettingsWidget::applySettings(QHelpFilterEngine
    #      *filterEngine) const
    return self.uglySide.call(
        'ritual_ZNK25QHelpFilterSettingsWidget13applySettingsEP17QHelpFilte'
        'rEngine',
        self._addressOf(filterEngine),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setAvailableComponents(self, components: QStringList) -> None:
    """
    Calls Qt's 'void QHelpFilterSettingsWidget::setAvailableComponents(const
    QStringList &components)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfiltersettingswidget.html

    Parameters
    ----------

    components : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QHelpFilterSettingsWidget::setAvailableComponents(const
    #      QStringList &components)
    self.uglySide.call(
        'ritual_ZN25QHelpFilterSettingsWidget22setAvailableComponentsERK5QL'
        'istI7QStringE',
        self._valueOf(components),
    )

  @overload(QList[QVersionNumber])
  def setAvailableVersions(self, versions: QList[QVersionNumber]) -> None:
    """
    Calls Qt's 'void QHelpFilterSettingsWidget::setAvailableVersions(const
    QList<QVersionNumber> &versions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfiltersettingswidget.html

    Parameters
    ----------

    versions : QList[QVersionNumber]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QHelpFilterSettingsWidget::setAvailableVersions(const
    #      QList<QVersionNumber> &versions)
    self.uglySide.call(
        'ritual_ZN25QHelpFilterSettingsWidget20setAvailableVersionsERK5QLis'
        'tI14QVersionNumberE',
        self._valueOf(versions),
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
    'QHelpFilterSettingsWidget::QHelpFilterSettingsWidget(QWidget *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfiltersettingswidget.html

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHelpFilterSettingsWidget::QHelpFilterSettingsWidget(QWidget *parent)
    self._noteCreation(QHelpFilterSettingsWidget, lambda: Rituals.call(
        'ritual_ZN25QHelpFilterSettingsWidgetC1EP7QWidget',
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

  @overload(QHelpFilterEngine)
  @overload(NoneType)
  def readSettings(self, filterEngine: Optional[QHelpFilterEngine]) -> None:
    """
    Calls Qt's 'void QHelpFilterSettingsWidget::readSettings(const
    QHelpFilterEngine *filterEngine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfiltersettingswidget.html#readSettings

    Parameters
    ----------

    filterEngine : Optional[QHelpFilterEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHelpFilterSettingsWidget::readSettings(const QHelpFilterEngine
    #      *filterEngine)
    self.uglySide.call(
        'ritual_ZN25QHelpFilterSettingsWidget12readSettingsEPK17QHelpFilter'
        'Engine',
        self._addressOf(filterEngine),
    )
