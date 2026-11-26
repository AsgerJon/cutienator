//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/glxyseriesdata_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/glxyseriesdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCharts/qabstractseries.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A GLXYSeriesDataManager that Python can take functions over in. Every GLXYSeriesDataManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteGLXYSeriesDataManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteGLXYSeriesDataManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteGLXYSeriesDataManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteGLXYSeriesDataManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteGLXYSeriesDataManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteGLXYSeriesDataManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteGLXYSeriesDataManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteGLXYSeriesDataManager : public GLXYSeriesDataManager {
public:
  using GLXYSeriesDataManager::GLXYSeriesDataManager;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteGLXYSeriesDataManagerCall0 call = reinterpret_cast<CuteGLXYSeriesDataManagerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteGLXYSeriesDataManagerCall1 call = reinterpret_cast<CuteGLXYSeriesDataManagerCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteGLXYSeriesDataManagerCall2 call = reinterpret_cast<CuteGLXYSeriesDataManagerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteGLXYSeriesDataManagerCall3 call = reinterpret_cast<CuteGLXYSeriesDataManagerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteGLXYSeriesDataManagerCall4 call = reinterpret_cast<CuteGLXYSeriesDataManagerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteGLXYSeriesDataManagerCall5 call = reinterpret_cast<CuteGLXYSeriesDataManagerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteGLXYSeriesDataManagerCall6 call = reinterpret_cast<CuteGLXYSeriesDataManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *GLXYSeriesDataManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21GLXYSeriesDataManager10metaObjectEv(
    const GLXYSeriesDataManager *self) {
  return self->metaObject();
}

//  void *GLXYSeriesDataManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21GLXYSeriesDataManager11qt_metacastEPKc(
    GLXYSeriesDataManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int GLXYSeriesDataManager::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21GLXYSeriesDataManager11qt_metacallEN11QMetaObject4CallEiPPv(
    GLXYSeriesDataManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString GLXYSeriesDataManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21GLXYSeriesDataManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(GLXYSeriesDataManager::tr(s, c, n));
}

//  GLXYSeriesDataManager::GLXYSeriesDataManager(QObject *parent)
extern "C" Q_DECL_EXPORT
GLXYSeriesDataManager *ritual_ZN21GLXYSeriesDataManagerC1EP7QObject(
    QObject *parent) {
  return new CuteGLXYSeriesDataManager(parent);
}

//  GLXYSeriesDataManager::~GLXYSeriesDataManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN21GLXYSeriesDataManagerD1Ev(GLXYSeriesDataManager *self) {
  delete self;
}

//  void GLXYSeriesDataManager::setPoints(QXYSeries *series, const
//      AbstractDomain *domain)
extern "C" Q_DECL_EXPORT
void ritual_ZN21GLXYSeriesDataManager9setPointsEP9QXYSeriesPK14AbstractDomain(
    GLXYSeriesDataManager *self,
    QXYSeries *series,
    const AbstractDomain *domain) {
  self->setPoints(series, domain);
}

//  void GLXYSeriesDataManager::removeSeries(const QXYSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN21GLXYSeriesDataManager12removeSeriesEPK9QXYSeries(
    GLXYSeriesDataManager *self,
    const QXYSeries *series) {
  self->removeSeries(series);
}

//  GLXYDataMap &GLXYSeriesDataManager::dataMap()
extern "C" Q_DECL_EXPORT
GLXYDataMap *ritual_ZN21GLXYSeriesDataManager7dataMapEv(
    GLXYSeriesDataManager *self) {
  return &(self->dataMap());
}

//  bool GLXYSeriesDataManager::mapDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21GLXYSeriesDataManager8mapDirtyEv(
    const GLXYSeriesDataManager *self) {
  return self->mapDirty();
}

//  void GLXYSeriesDataManager::clearAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN21GLXYSeriesDataManager13clearAllDirtyEv(
    GLXYSeriesDataManager *self) {
  self->clearAllDirty();
}

//  void GLXYSeriesDataManager::handleAxisReverseChanged(const
//      QList<QAbstractSeries *> &seriesList)
extern "C" Q_DECL_EXPORT
void ritual_ZN21GLXYSeriesDataManager24handleAxisReverseChangedERK5QListIP15QAbstractSeriesE(
    GLXYSeriesDataManager *self,
    const QList<QAbstractSeries *> *seriesList) {
  self->handleAxisReverseChanged(*seriesList);
}

//  void GLXYSeriesDataManager::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN21GLXYSeriesDataManager7cleanupEv(
    GLXYSeriesDataManager *self) {
  self->cleanup();
}

//  void GLXYSeriesDataManager::handleSeriesPenChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN21GLXYSeriesDataManager21handleSeriesPenChangeEv(
    GLXYSeriesDataManager *self) {
  self->handleSeriesPenChange();
}

//  void GLXYSeriesDataManager::handleSeriesOpenGLChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN21GLXYSeriesDataManager24handleSeriesOpenGLChangeEv(
    GLXYSeriesDataManager *self) {
  self->handleSeriesOpenGLChange();
}

//  void GLXYSeriesDataManager::handleSeriesVisibilityChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN21GLXYSeriesDataManager28handleSeriesVisibilityChangeEv(
    GLXYSeriesDataManager *self) {
  self->handleSeriesVisibilityChange();
}

#if QT_CONFIG(charts_scatter_chart)
//  void GLXYSeriesDataManager::handleScatterColorChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN21GLXYSeriesDataManager24handleScatterColorChangeEv(
    GLXYSeriesDataManager *self) {
  self->handleScatterColorChange();
}
#endif  // QT_CONFIG(charts_scatter_chart)

#if QT_CONFIG(charts_scatter_chart)
//  void GLXYSeriesDataManager::handleScatterMarkerSizeChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN21GLXYSeriesDataManager29handleScatterMarkerSizeChangeEv(
    GLXYSeriesDataManager *self) {
  self->handleScatterMarkerSizeChange();
}
#endif  // QT_CONFIG(charts_scatter_chart)

//  void GLXYSeriesDataManager::seriesRemoved(const QXYSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN21GLXYSeriesDataManager13seriesRemovedEPK9QXYSeries(
    GLXYSeriesDataManager *self,
    const QXYSeries *series) {
  self->seriesRemoved(series);
}

//  a Python function taken by a CuteGLXYSeriesDataManager, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_GLXYSeriesDataManager(
    GLXYSeriesDataManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteGLXYSeriesDataManager *>(self)->take(key, call);
}
