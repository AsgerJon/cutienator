//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qgeoareamonitorsource.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtPositioning/qgeoareamonitorsource.h>
#include <QtCore/qstring.h>
#include <QtPositioning/qgeoareamonitorinfo.h>
#include <QtPositioning/qgeoshape.h>
#include <QtCore/qvariant.h>
#include <QtPositioning/qgeopositioninfo.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QGeoAreaMonitorSource that Python can take functions over in. Every QGeoAreaMonitorSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGeoAreaMonitorSourceCall0)(const void *, QGeoPositionInfoSource *, int *);
typedef void * (*CuteQGeoAreaMonitorSourceCall1)(const void *, int *);
typedef int (*CuteQGeoAreaMonitorSourceCall2)(const void *, int *);
typedef int (*CuteQGeoAreaMonitorSourceCall3)(const void *, int *);
typedef bool (*CuteQGeoAreaMonitorSourceCall4)(const void *, const QGeoAreaMonitorInfo *, int *);
typedef bool (*CuteQGeoAreaMonitorSourceCall5)(const void *, const QGeoAreaMonitorInfo *, int *);
typedef bool (*CuteQGeoAreaMonitorSourceCall6)(const void *, const QString *, const QVariant *, int *);
typedef const QVariant * (*CuteQGeoAreaMonitorSourceCall7)(const void *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoAreaMonitorSourceCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoAreaMonitorSourceCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoAreaMonitorSourceCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoAreaMonitorSourceCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoAreaMonitorSourceCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoAreaMonitorSourceCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoAreaMonitorSourceCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoAreaMonitorSource : public QGeoAreaMonitorSource {
public:
  using QGeoAreaMonitorSource::QGeoAreaMonitorSource;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QGeoAreaMonitorSource21setPositionInfoSourceEP22QGeoPositionInfoSource")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QGeoAreaMonitorSource18positionInfoSourceEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QGeoAreaMonitorSource5errorEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QGeoAreaMonitorSource28supportedAreaMonitorFeaturesEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QGeoAreaMonitorSource15startMonitoringERK19QGeoAreaMonitorInfo")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QGeoAreaMonitorSource14stopMonitoringERK19QGeoAreaMonitorInfo")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QGeoAreaMonitorSource18setBackendPropertyERK7QStringRK8QVariant")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QGeoAreaMonitorSource15backendPropertyERK7QString")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void
  //      QGeoAreaMonitorSource::setPositionInfoSource(QGeoPositionInfoSour
  //      ce *source)
  void setPositionInfoSource(QGeoPositionInfoSource *source) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoAreaMonitorSourceCall0 call = reinterpret_cast<CuteQGeoAreaMonitorSourceCall0>(taken[0]);
      call(this, source, &handled);
      if (handled) return;
    }
    QGeoAreaMonitorSource::setPositionInfoSource(source);
  }

  //  QGeoPositionInfoSource *QGeoAreaMonitorSource::positionInfoSource()
  //      const
  QGeoPositionInfoSource *positionInfoSource() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoAreaMonitorSourceCall1 call = reinterpret_cast<CuteQGeoAreaMonitorSourceCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QGeoPositionInfoSource *>(given);
    }
    return QGeoAreaMonitorSource::positionInfoSource();
  }

  //  Error QGeoAreaMonitorSource::error() const
  QGeoAreaMonitorSource::Error error() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoAreaMonitorSourceCall2 call = reinterpret_cast<CuteQGeoAreaMonitorSourceCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QGeoAreaMonitorSource::Error>(given);
    }
    return {};
  }

  //  AreaMonitorFeatures
  //      QGeoAreaMonitorSource::supportedAreaMonitorFeatures() const
  QGeoAreaMonitorSource::AreaMonitorFeatures supportedAreaMonitorFeatures() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoAreaMonitorSourceCall3 call = reinterpret_cast<CuteQGeoAreaMonitorSourceCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return QFlags<QGeoAreaMonitorSource::AreaMonitorFeature>::fromInt(given);
    }
    return {};
  }

  //  bool QGeoAreaMonitorSource::startMonitoring(const QGeoAreaMonitorInfo
  //      &monitor)
  bool startMonitoring(const QGeoAreaMonitorInfo &monitor) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoAreaMonitorSourceCall4 call = reinterpret_cast<CuteQGeoAreaMonitorSourceCall4>(taken[4]);
      bool given = call(this, &monitor, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QGeoAreaMonitorSource::stopMonitoring(const QGeoAreaMonitorInfo
  //      &monitor)
  bool stopMonitoring(const QGeoAreaMonitorInfo &monitor) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoAreaMonitorSourceCall5 call = reinterpret_cast<CuteQGeoAreaMonitorSourceCall5>(taken[5]);
      bool given = call(this, &monitor, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QGeoAreaMonitorSource::setBackendProperty(const QString &name,
  //      const QVariant &value)
  bool setBackendProperty(
      const QString &name,
      const QVariant &value) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoAreaMonitorSourceCall6 call = reinterpret_cast<CuteQGeoAreaMonitorSourceCall6>(taken[6]);
      bool given = call(this, &name, &value, &handled);
      if (handled) return given;
    }
    return QGeoAreaMonitorSource::setBackendProperty(name, value);
  }

  //  QVariant QGeoAreaMonitorSource::backendProperty(const QString &name)
  //      const
  QVariant backendProperty(const QString &name) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGeoAreaMonitorSourceCall7 call = reinterpret_cast<CuteQGeoAreaMonitorSourceCall7>(taken[7]);
      const QVariant * given = call(this, &name, &handled);
      if (handled && given) return *given;
    }
    return QGeoAreaMonitorSource::backendProperty(name);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGeoAreaMonitorSourceCall8 call = reinterpret_cast<CuteQGeoAreaMonitorSourceCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGeoAreaMonitorSourceCall9 call = reinterpret_cast<CuteQGeoAreaMonitorSourceCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQGeoAreaMonitorSourceCall10 call = reinterpret_cast<CuteQGeoAreaMonitorSourceCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQGeoAreaMonitorSourceCall11 call = reinterpret_cast<CuteQGeoAreaMonitorSourceCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGeoAreaMonitorSourceCall12 call = reinterpret_cast<CuteQGeoAreaMonitorSourceCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQGeoAreaMonitorSourceCall13 call = reinterpret_cast<CuteQGeoAreaMonitorSourceCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQGeoAreaMonitorSourceCall14 call = reinterpret_cast<CuteQGeoAreaMonitorSourceCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoAreaMonitorSource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QGeoAreaMonitorSource10metaObjectEv(
    const QGeoAreaMonitorSource *self) {
  return self->metaObject();
}

//  void *QGeoAreaMonitorSource::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QGeoAreaMonitorSource11qt_metacastEPKc(
    QGeoAreaMonitorSource *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGeoAreaMonitorSource::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QGeoAreaMonitorSource11qt_metacallEN11QMetaObject4CallEiPPv(
    QGeoAreaMonitorSource *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGeoAreaMonitorSource::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QGeoAreaMonitorSource2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoAreaMonitorSource::tr(s, c, n));
}

//  QGeoAreaMonitorSource::~QGeoAreaMonitorSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGeoAreaMonitorSourceD1Ev(QGeoAreaMonitorSource *self) {
  delete self;
}

//  QGeoAreaMonitorSource *QGeoAreaMonitorSource::createDefaultSource(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QGeoAreaMonitorSource *ritual_ZN21QGeoAreaMonitorSource19createDefaultSourceEP7QObject(
    QObject *parent) {
  return QGeoAreaMonitorSource::createDefaultSource(parent);
}

//  QGeoAreaMonitorSource *QGeoAreaMonitorSource::createSource(const QString
//      &sourceName, QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoAreaMonitorSource *ritual_ZN21QGeoAreaMonitorSource12createSourceERK7QStringP7QObject(
    const QString *sourceName,
    QObject *parent) {
  return QGeoAreaMonitorSource::createSource(*sourceName, parent);
}

//  QStringList QGeoAreaMonitorSource::availableSources()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN21QGeoAreaMonitorSource16availableSourcesEv() {
  return new QList<QString>(QGeoAreaMonitorSource::availableSources());
}

//  void QGeoAreaMonitorSource::setPositionInfoSource(QGeoPositionInfoSource
//      *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGeoAreaMonitorSource21setPositionInfoSourceEP22QGeoPositionInfoSource(
    QGeoAreaMonitorSource *self,
    QGeoPositionInfoSource *source) {
  self->setPositionInfoSource(source);
}

//  QGeoPositionInfoSource *QGeoAreaMonitorSource::positionInfoSource() const
extern "C" Q_DECL_EXPORT
QGeoPositionInfoSource *ritual_ZNK21QGeoAreaMonitorSource18positionInfoSourceEv(
    const QGeoAreaMonitorSource *self) {
  return self->positionInfoSource();
}

//  QString QGeoAreaMonitorSource::sourceName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QGeoAreaMonitorSource10sourceNameEv(
    const QGeoAreaMonitorSource *self) {
  return new QString(self->sourceName());
}

//  Error QGeoAreaMonitorSource::error() const
extern "C" Q_DECL_EXPORT
QGeoAreaMonitorSource::Error ritual_ZNK21QGeoAreaMonitorSource5errorEv(
    const QGeoAreaMonitorSource *self) {
  return self->error();
}

//  AreaMonitorFeatures QGeoAreaMonitorSource::supportedAreaMonitorFeatures()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QGeoAreaMonitorSource28supportedAreaMonitorFeaturesEv(
    const QGeoAreaMonitorSource *self) {
  return static_cast<int>(self->supportedAreaMonitorFeatures().toInt());
}

//  bool QGeoAreaMonitorSource::startMonitoring(const QGeoAreaMonitorInfo
//      &monitor)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QGeoAreaMonitorSource15startMonitoringERK19QGeoAreaMonitorInfo(
    QGeoAreaMonitorSource *self,
    const QGeoAreaMonitorInfo *monitor) {
  return self->startMonitoring(*monitor);
}

//  bool QGeoAreaMonitorSource::stopMonitoring(const QGeoAreaMonitorInfo
//      &monitor)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QGeoAreaMonitorSource14stopMonitoringERK19QGeoAreaMonitorInfo(
    QGeoAreaMonitorSource *self,
    const QGeoAreaMonitorInfo *monitor) {
  return self->stopMonitoring(*monitor);
}

//  bool QGeoAreaMonitorSource::requestUpdate(const QGeoAreaMonitorInfo
//      &monitor, const char *signal)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QGeoAreaMonitorSource13requestUpdateERK19QGeoAreaMonitorInfoPKc(
    QGeoAreaMonitorSource *self,
    const QGeoAreaMonitorInfo *monitor,
    const char *signal) {
  return self->requestUpdate(*monitor, signal);
}

//  QList<QGeoAreaMonitorInfo> QGeoAreaMonitorSource::activeMonitors() const
extern "C" Q_DECL_EXPORT
QList<QGeoAreaMonitorInfo> *ritual_ZNK21QGeoAreaMonitorSource14activeMonitorsEv(
    const QGeoAreaMonitorSource *self) {
  return new QList<QGeoAreaMonitorInfo>(self->activeMonitors());
}

//  QList<QGeoAreaMonitorInfo> QGeoAreaMonitorSource::activeMonitors(const
//      QGeoShape &lookupArea) const
extern "C" Q_DECL_EXPORT
QList<QGeoAreaMonitorInfo> *ritual_ZNK21QGeoAreaMonitorSource14activeMonitorsERK9QGeoShape(
    const QGeoAreaMonitorSource *self,
    const QGeoShape *lookupArea) {
  return new QList<QGeoAreaMonitorInfo>(self->activeMonitors(*lookupArea));
}

//  bool QGeoAreaMonitorSource::setBackendProperty(const QString &name, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QGeoAreaMonitorSource18setBackendPropertyERK7QStringRK8QVariant(
    QGeoAreaMonitorSource *self,
    const QString *name,
    const QVariant *value) {
  return self->setBackendProperty(*name, *value);
}

//  QVariant QGeoAreaMonitorSource::backendProperty(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QGeoAreaMonitorSource15backendPropertyERK7QString(
    const QGeoAreaMonitorSource *self,
    const QString *name) {
  return new QVariant(self->backendProperty(*name));
}

//  void QGeoAreaMonitorSource::areaEntered(const QGeoAreaMonitorInfo
//      &monitor, const QGeoPositionInfo &update)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGeoAreaMonitorSource11areaEnteredERK19QGeoAreaMonitorInfoRK16QGeoPositionInfo(
    QGeoAreaMonitorSource *self,
    const QGeoAreaMonitorInfo *monitor,
    const QGeoPositionInfo *update) {
  self->areaEntered(*monitor, *update);
}

//  void QGeoAreaMonitorSource::areaExited(const QGeoAreaMonitorInfo
//      &monitor, const QGeoPositionInfo &update)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGeoAreaMonitorSource10areaExitedERK19QGeoAreaMonitorInfoRK16QGeoPositionInfo(
    QGeoAreaMonitorSource *self,
    const QGeoAreaMonitorInfo *monitor,
    const QGeoPositionInfo *update) {
  self->areaExited(*monitor, *update);
}

//  void QGeoAreaMonitorSource::monitorExpired(const QGeoAreaMonitorInfo
//      &monitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGeoAreaMonitorSource14monitorExpiredERK19QGeoAreaMonitorInfo(
    QGeoAreaMonitorSource *self,
    const QGeoAreaMonitorInfo *monitor) {
  self->monitorExpired(*monitor);
}

//  void QGeoAreaMonitorSource::errorOccurred(QGeoAreaMonitorSource::Error
//      error)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGeoAreaMonitorSource13errorOccurredENS_5ErrorE(
    QGeoAreaMonitorSource *self,
    QGeoAreaMonitorSource::Error error) {
  self->errorOccurred(error);
}

//  QGeoAreaMonitorSourcePrivate *QGeoAreaMonitorSource::d_func()
extern "C" Q_DECL_EXPORT
QGeoAreaMonitorSourcePrivate *ritual_ZN21QGeoAreaMonitorSource6d_funcEv(
    QGeoAreaMonitorSource *self) {
  return self->d_func();
}

//  const QGeoAreaMonitorSourcePrivate *QGeoAreaMonitorSource::d_func() const
extern "C" Q_DECL_EXPORT
const QGeoAreaMonitorSourcePrivate *ritual_ZNK21QGeoAreaMonitorSource6d_funcEv(
    const QGeoAreaMonitorSource *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGeoAreaMonitorSource, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoAreaMonitorSource(
    QGeoAreaMonitorSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoAreaMonitorSource *>(self)->take(key, call);
}

//  void QGeoAreaMonitorSource::setPositionInfoSource(QGeoPositionInfoSource
//      *source)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QGeoAreaMonitorSource21setPositionInfoSourceEP22QGeoPositionInfoSource(
    QGeoAreaMonitorSource *self,
    QGeoPositionInfoSource *source) {
  self->QGeoAreaMonitorSource::setPositionInfoSource(source);
}

//  QGeoPositionInfoSource *QGeoAreaMonitorSource::positionInfoSource() const
extern "C" Q_DECL_EXPORT
QGeoPositionInfoSource *ritual_own_ZNK21QGeoAreaMonitorSource18positionInfoSourceEv(
    const QGeoAreaMonitorSource *self) {
  return self->QGeoAreaMonitorSource::positionInfoSource();
}

//  bool QGeoAreaMonitorSource::setBackendProperty(const QString &name, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QGeoAreaMonitorSource18setBackendPropertyERK7QStringRK8QVariant(
    QGeoAreaMonitorSource *self,
    const QString *name,
    const QVariant *value) {
  return self->QGeoAreaMonitorSource::setBackendProperty(*name, *value);
}

//  QVariant QGeoAreaMonitorSource::backendProperty(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK21QGeoAreaMonitorSource15backendPropertyERK7QString(
    const QGeoAreaMonitorSource *self,
    const QString *name) {
  return new QVariant(self->QGeoAreaMonitorSource::backendProperty(*name));
}
