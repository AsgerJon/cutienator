"""
GLXYSeriesDataManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/glxyseriesdata_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means GLXYSeriesDataManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import AbstractDomain, QAbstractSeries, QXYSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  AbstractDomain = WAIT['AbstractDomain']
  QAbstractSeries = WAIT['QtCharts:QAbstractSeries']
  QXYSeries = WAIT['QtCharts:QXYSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class GLXYSeriesDataManager(QObject):
  """
  The cute side of Qt's GLXYSeriesDataManager: a plain Python object standing
  in front of one C++ GLXYSeriesDataManager.

  It is built on the cute 'QObject', as Qt's GLXYSeriesDataManager is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's GLXYSeriesDataManager that has a ritual and that
  Python can call so far, 14 names in all: 'metaObject', 'tr', 'setPoints',
  'removeSeries', 'mapDirty', 'clearAllDirty', 'handleAxisReverseChanged',
  'cleanup', 'handleSeriesPenChange', 'handleSeriesOpenGLChange',
  'handleSeriesVisibilityChange', 'handleScatterColorChange',
  'handleScatterMarkerSizeChange', 'seriesRemoved'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *GLXYSeriesDataManager::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int GLXYSeriesDataManager::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'GLXYSeriesDataManager::~GLXYSeriesDataManager()': the destructor:
    Python never removes a C++ GLXYSeriesDataManager.
  - Qt's 'GLXYDataMap &GLXYSeriesDataManager::dataMap()': gives a type Python
    has no way to take yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ GLXYSeriesDataManager is created at the first use, not by
    'GLXYSeriesDataManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ GLXYSeriesDataManager.
  - Qt tells when it has removed the C++ GLXYSeriesDataManager. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's GLXYSeriesDataManager that has no cute function yet,
    'dataMap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString GLXYSeriesDataManager::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/glxyseriesdatamanager.html#tr

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
    #  QString GLXYSeriesDataManager::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21GLXYSeriesDataManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'GLXYSeriesDataManager'

  #  A C++ GLXYSeriesDataManager Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_GLXYSeriesDataManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *GLXYSeriesDataManager::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/glxyseriesdatamanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *GLXYSeriesDataManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21GLXYSeriesDataManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def mapDirty(self) -> bool:
    """
    Calls Qt's 'bool GLXYSeriesDataManager::mapDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/glxyseriesdatamanager.html#mapDirty
    """
    #  bool GLXYSeriesDataManager::mapDirty() const
    return self.uglySide.call('ritual_ZNK21GLXYSeriesDataManager8mapDirtyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QXYSeries, AbstractDomain)
  @overload(QXYSeries, NoneType)
  @overload(NoneType, AbstractDomain)
  @overload(NoneType, NoneType)
  def setPoints(
      self,
      series: Optional[QXYSeries],
      domain: Optional[AbstractDomain],
  ) -> None:
    """
    Calls Qt's 'void GLXYSeriesDataManager::setPoints(QXYSeries *series,
    const AbstractDomain *domain)'.

    Qt's own words:
    https://doc.qt.io/qt-6/glxyseriesdatamanager.html#setPoints

    Parameters
    ----------

    series : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    domain : Optional[AbstractDomain]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void GLXYSeriesDataManager::setPoints(QXYSeries *series, const
    #      AbstractDomain *domain)
    self.uglySide.call(
        'ritual_ZN21GLXYSeriesDataManager9setPointsEP9QXYSeriesPK14Abstract'
        'Domain',
        self._addressOf(series), self._addressOf(domain),
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
    'GLXYSeriesDataManager::GLXYSeriesDataManager(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/glxyseriesdatamanager.html#GLXYSeriesDataManager

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  GLXYSeriesDataManager::GLXYSeriesDataManager(QObject *parent)
    self._noteCreation(GLXYSeriesDataManager, lambda: Rituals.call(
        'ritual_ZN21GLXYSeriesDataManagerC1EP7QObject',
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

  @overload(QXYSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QXYSeries]) -> None:
    """
    Calls Qt's 'void GLXYSeriesDataManager::removeSeries(const QXYSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/glxyseriesdatamanager.html#removeSeries

    Parameters
    ----------

    series : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void GLXYSeriesDataManager::removeSeries(const QXYSeries *series)
    self.uglySide.call(
        'ritual_ZN21GLXYSeriesDataManager12removeSeriesEPK9QXYSeries',
        self._addressOf(series),
    )

  def clearAllDirty(self) -> None:
    """
    Calls Qt's 'void GLXYSeriesDataManager::clearAllDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/glxyseriesdatamanager.html#clearAllDirty
    """
    #  void GLXYSeriesDataManager::clearAllDirty()
    self.uglySide.call('ritual_ZN21GLXYSeriesDataManager13clearAllDirtyEv')

  @overload(QList[QAbstractSeries])
  def handleAxisReverseChanged(
      self,
      seriesList: QList[QAbstractSeries],
  ) -> None:
    """
    Calls Qt's 'void GLXYSeriesDataManager::handleAxisReverseChanged(const
    QList<QAbstractSeries *> &seriesList)'.

    Qt's own words:
    https://doc.qt.io/qt-6/glxyseriesdatamanager.html

    Parameters
    ----------

    seriesList : QList[QAbstractSeries]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void GLXYSeriesDataManager::handleAxisReverseChanged(const
    #      QList<QAbstractSeries *> &seriesList)
    self.uglySide.call(
        'ritual_ZN21GLXYSeriesDataManager24handleAxisReverseChangedERK5QLis'
        'tIP15QAbstractSeriesE',
        self._valueOf(seriesList),
    )

  def cleanup(self) -> None:
    """
    Calls Qt's 'void GLXYSeriesDataManager::cleanup()'.

    Qt's own words: https://doc.qt.io/qt-6/glxyseriesdatamanager.html#cleanup
    """
    #  void GLXYSeriesDataManager::cleanup()
    self.uglySide.call('ritual_ZN21GLXYSeriesDataManager7cleanupEv')

  def handleSeriesPenChange(self) -> None:
    """
    Calls Qt's 'void GLXYSeriesDataManager::handleSeriesPenChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/glxyseriesdatamanager.html#handleSeriesPenChange
    """
    #  void GLXYSeriesDataManager::handleSeriesPenChange()
    self.uglySide.call(
        'ritual_ZN21GLXYSeriesDataManager21handleSeriesPenChangeEv',
    )

  def handleSeriesOpenGLChange(self) -> None:
    """
    Calls Qt's 'void GLXYSeriesDataManager::handleSeriesOpenGLChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/glxyseriesdatamanager.html
    """
    #  void GLXYSeriesDataManager::handleSeriesOpenGLChange()
    self.uglySide.call(
        'ritual_ZN21GLXYSeriesDataManager24handleSeriesOpenGLChangeEv',
    )

  def handleSeriesVisibilityChange(self) -> None:
    """
    Calls Qt's 'void GLXYSeriesDataManager::handleSeriesVisibilityChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/glxyseriesdatamanager.html
    """
    #  void GLXYSeriesDataManager::handleSeriesVisibilityChange()
    self.uglySide.call(
        'ritual_ZN21GLXYSeriesDataManager28handleSeriesVisibilityChangeEv',
    )

  def handleScatterColorChange(self) -> None:
    """
    Calls Qt's 'void GLXYSeriesDataManager::handleScatterColorChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/glxyseriesdatamanager.html
    """
    #  void GLXYSeriesDataManager::handleScatterColorChange()
    self.uglySide.call(
        'ritual_ZN21GLXYSeriesDataManager24handleScatterColorChangeEv',
    )

  def handleScatterMarkerSizeChange(self) -> None:
    """
    Calls Qt's 'void GLXYSeriesDataManager::handleScatterMarkerSizeChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/glxyseriesdatamanager.html
    """
    #  void GLXYSeriesDataManager::handleScatterMarkerSizeChange()
    self.uglySide.call(
        'ritual_ZN21GLXYSeriesDataManager29handleScatterMarkerSizeChangeEv',
    )

  @overload(QXYSeries)
  @overload(NoneType)
  def seriesRemoved(self, series: Optional[QXYSeries]) -> None:
    """
    Calls Qt's 'void GLXYSeriesDataManager::seriesRemoved(const QXYSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/glxyseriesdatamanager.html#seriesRemoved

    Parameters
    ----------

    series : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void GLXYSeriesDataManager::seriesRemoved(const QXYSeries *series)
    self.uglySide.call(
        'ritual_ZN21GLXYSeriesDataManager13seriesRemovedEPK9QXYSeries',
        self._addressOf(series),
    )

  @staticmethod
  def dataMap(*__, **_) -> Never:
    """
    Qt's 'GLXYDataMap &GLXYSeriesDataManager::dataMap()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'GLXYSeriesDataManager.dataMap' has no cute function yet. Qt's "
        "'GLXYDataMap &GLXYSeriesDataManager::dataMap()': gives a type "
        "Python has no way to take yet.")
