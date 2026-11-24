//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qgeosatelliteinfosource.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtPositioning/qgeosatelliteinfosource.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QGeoSatelliteInfoSource that Python can take functions over in. Every QGeoSatelliteInfoSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGeoSatelliteInfoSourceCall0)(const void *, int, int *);
typedef int (*CuteQGeoSatelliteInfoSourceCall1)(const void *, int *);
typedef int (*CuteQGeoSatelliteInfoSourceCall2)(const void *, int *);
typedef bool (*CuteQGeoSatelliteInfoSourceCall3)(const void *, const QString *, const QVariant *, int *);
typedef const QVariant * (*CuteQGeoSatelliteInfoSourceCall4)(const void *, const QString *, int *);
typedef void (*CuteQGeoSatelliteInfoSourceCall5)(const void *, int *);
typedef void (*CuteQGeoSatelliteInfoSourceCall6)(const void *, int *);
typedef void (*CuteQGeoSatelliteInfoSourceCall7)(const void *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoSatelliteInfoSourceCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoSatelliteInfoSourceCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoSatelliteInfoSourceCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoSatelliteInfoSourceCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoSatelliteInfoSourceCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoSatelliteInfoSourceCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoSatelliteInfoSourceCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoSatelliteInfoSource : public QGeoSatelliteInfoSource {
public:
  using QGeoSatelliteInfoSource::QGeoSatelliteInfoSource;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QGeoSatelliteInfoSource17setUpdateIntervalEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QGeoSatelliteInfoSource21minimumUpdateIntervalEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QGeoSatelliteInfoSource5errorEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QGeoSatelliteInfoSource18setBackendPropertyERK7QStringRK8QVariant")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QGeoSatelliteInfoSource15backendPropertyERK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QGeoSatelliteInfoSource12startUpdatesEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QGeoSatelliteInfoSource11stopUpdatesEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QGeoSatelliteInfoSource13requestUpdateEi")) {
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

  //  void QGeoSatelliteInfoSource::setUpdateInterval(int msec)
  void setUpdateInterval(int msec) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoSatelliteInfoSourceCall0 call = reinterpret_cast<CuteQGeoSatelliteInfoSourceCall0>(taken[0]);
      call(this, msec, &handled);
      if (handled) return;
    }
    QGeoSatelliteInfoSource::setUpdateInterval(msec);
  }

  //  int QGeoSatelliteInfoSource::minimumUpdateInterval() const
  int minimumUpdateInterval() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoSatelliteInfoSourceCall1 call = reinterpret_cast<CuteQGeoSatelliteInfoSourceCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  Error QGeoSatelliteInfoSource::error() const
  QGeoSatelliteInfoSource::Error error() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoSatelliteInfoSourceCall2 call = reinterpret_cast<CuteQGeoSatelliteInfoSourceCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QGeoSatelliteInfoSource::Error>(given);
    }
    return {};
  }

  //  bool QGeoSatelliteInfoSource::setBackendProperty(const QString &name,
  //      const QVariant &value)
  bool setBackendProperty(
      const QString &name,
      const QVariant &value) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoSatelliteInfoSourceCall3 call = reinterpret_cast<CuteQGeoSatelliteInfoSourceCall3>(taken[3]);
      bool given = call(this, &name, &value, &handled);
      if (handled) return given;
    }
    return QGeoSatelliteInfoSource::setBackendProperty(name, value);
  }

  //  QVariant QGeoSatelliteInfoSource::backendProperty(const QString
  //      &name) const
  QVariant backendProperty(const QString &name) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoSatelliteInfoSourceCall4 call = reinterpret_cast<CuteQGeoSatelliteInfoSourceCall4>(taken[4]);
      const QVariant * given = call(this, &name, &handled);
      if (handled && given) return *given;
    }
    return QGeoSatelliteInfoSource::backendProperty(name);
  }

  //  void QGeoSatelliteInfoSource::startUpdates()
  void startUpdates() override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoSatelliteInfoSourceCall5 call = reinterpret_cast<CuteQGeoSatelliteInfoSourceCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QGeoSatelliteInfoSource::stopUpdates()
  void stopUpdates() override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoSatelliteInfoSourceCall6 call = reinterpret_cast<CuteQGeoSatelliteInfoSourceCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QGeoSatelliteInfoSource::requestUpdate(int timeout)
  void requestUpdate(int timeout) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGeoSatelliteInfoSourceCall7 call = reinterpret_cast<CuteQGeoSatelliteInfoSourceCall7>(taken[7]);
      call(this, timeout, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGeoSatelliteInfoSourceCall8 call = reinterpret_cast<CuteQGeoSatelliteInfoSourceCall8>(taken[8]);
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
      CuteQGeoSatelliteInfoSourceCall9 call = reinterpret_cast<CuteQGeoSatelliteInfoSourceCall9>(taken[9]);
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
      CuteQGeoSatelliteInfoSourceCall10 call = reinterpret_cast<CuteQGeoSatelliteInfoSourceCall10>(taken[10]);
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
      CuteQGeoSatelliteInfoSourceCall11 call = reinterpret_cast<CuteQGeoSatelliteInfoSourceCall11>(taken[11]);
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
      CuteQGeoSatelliteInfoSourceCall12 call = reinterpret_cast<CuteQGeoSatelliteInfoSourceCall12>(taken[12]);
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
      CuteQGeoSatelliteInfoSourceCall13 call = reinterpret_cast<CuteQGeoSatelliteInfoSourceCall13>(taken[13]);
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
      CuteQGeoSatelliteInfoSourceCall14 call = reinterpret_cast<CuteQGeoSatelliteInfoSourceCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoSatelliteInfoSource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QGeoSatelliteInfoSource10metaObjectEv(
    const QGeoSatelliteInfoSource *self) {
  return self->metaObject();
}

//  QString QGeoSatelliteInfoSource::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QGeoSatelliteInfoSource2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoSatelliteInfoSource::tr(s, c, n));
}

//  QGeoSatelliteInfoSource::~QGeoSatelliteInfoSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoSatelliteInfoSourceD1Ev(QGeoSatelliteInfoSource *self) {
  delete self;
}

//  QGeoSatelliteInfoSource
//      *QGeoSatelliteInfoSource::createDefaultSource(QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoSatelliteInfoSource *ritual_ZN23QGeoSatelliteInfoSource19createDefaultSourceEP7QObject(
    QObject *parent) {
  return QGeoSatelliteInfoSource::createDefaultSource(parent);
}

//  QGeoSatelliteInfoSource *QGeoSatelliteInfoSource::createSource(const
//      QString &sourceName, QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoSatelliteInfoSource *ritual_ZN23QGeoSatelliteInfoSource12createSourceERK7QStringP7QObject(
    const QString *sourceName,
    QObject *parent) {
  return QGeoSatelliteInfoSource::createSource(*sourceName, parent);
}

//  QGeoSatelliteInfoSource
//      *QGeoSatelliteInfoSource::createDefaultSource(const QVariantMap
//      &parameters, QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoSatelliteInfoSource *ritual_ZN23QGeoSatelliteInfoSource19createDefaultSourceERK4QMapI7QString8QVariantEP7QObject(
    const QMap<QString, QVariant> *parameters,
    QObject *parent) {
  return QGeoSatelliteInfoSource::createDefaultSource(*parameters, parent);
}

//  QGeoSatelliteInfoSource *QGeoSatelliteInfoSource::createSource(const
//      QString &sourceName, const QVariantMap &parameters, QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoSatelliteInfoSource *ritual_ZN23QGeoSatelliteInfoSource12createSourceERK7QStringRK4QMapIS0_8QVariantEP7QObject(
    const QString *sourceName,
    const QMap<QString, QVariant> *parameters,
    QObject *parent) {
  return QGeoSatelliteInfoSource::createSource(
      *sourceName,
      *parameters,
      parent);
}

//  QStringList QGeoSatelliteInfoSource::availableSources()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN23QGeoSatelliteInfoSource16availableSourcesEv() {
  return new QList<QString>(QGeoSatelliteInfoSource::availableSources());
}

//  QString QGeoSatelliteInfoSource::sourceName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QGeoSatelliteInfoSource10sourceNameEv(
    const QGeoSatelliteInfoSource *self) {
  return new QString(self->sourceName());
}

//  void QGeoSatelliteInfoSource::setUpdateInterval(int msec)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoSatelliteInfoSource17setUpdateIntervalEi(
    QGeoSatelliteInfoSource *self,
    int msec) {
  self->setUpdateInterval(msec);
}

//  int QGeoSatelliteInfoSource::updateInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QGeoSatelliteInfoSource14updateIntervalEv(
    const QGeoSatelliteInfoSource *self) {
  return self->updateInterval();
}

//  int QGeoSatelliteInfoSource::minimumUpdateInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QGeoSatelliteInfoSource21minimumUpdateIntervalEv(
    const QGeoSatelliteInfoSource *self) {
  return self->minimumUpdateInterval();
}

//  Error QGeoSatelliteInfoSource::error() const
extern "C" Q_DECL_EXPORT
QGeoSatelliteInfoSource::Error ritual_ZNK23QGeoSatelliteInfoSource5errorEv(
    const QGeoSatelliteInfoSource *self) {
  return self->error();
}

//  bool QGeoSatelliteInfoSource::setBackendProperty(const QString &name,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QGeoSatelliteInfoSource18setBackendPropertyERK7QStringRK8QVariant(
    QGeoSatelliteInfoSource *self,
    const QString *name,
    const QVariant *value) {
  return self->setBackendProperty(*name, *value);
}

//  QVariant QGeoSatelliteInfoSource::backendProperty(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QGeoSatelliteInfoSource15backendPropertyERK7QString(
    const QGeoSatelliteInfoSource *self,
    const QString *name) {
  return new QVariant(self->backendProperty(*name));
}

//  void QGeoSatelliteInfoSource::startUpdates()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoSatelliteInfoSource12startUpdatesEv(
    QGeoSatelliteInfoSource *self) {
  self->startUpdates();
}

//  void QGeoSatelliteInfoSource::stopUpdates()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoSatelliteInfoSource11stopUpdatesEv(
    QGeoSatelliteInfoSource *self) {
  self->stopUpdates();
}

//  void QGeoSatelliteInfoSource::requestUpdate(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoSatelliteInfoSource13requestUpdateEi(
    QGeoSatelliteInfoSource *self,
    int timeout) {
  self->requestUpdate(timeout);
}

//  QGeoSatelliteInfoSourcePrivate *QGeoSatelliteInfoSource::d_func()
extern "C" Q_DECL_EXPORT
QGeoSatelliteInfoSourcePrivate *ritual_ZN23QGeoSatelliteInfoSource6d_funcEv(
    QGeoSatelliteInfoSource *self) {
  return self->d_func();
}

//  const QGeoSatelliteInfoSourcePrivate *QGeoSatelliteInfoSource::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QGeoSatelliteInfoSourcePrivate *ritual_ZNK23QGeoSatelliteInfoSource6d_funcEv(
    const QGeoSatelliteInfoSource *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGeoSatelliteInfoSource, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoSatelliteInfoSource(
    QGeoSatelliteInfoSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoSatelliteInfoSource *>(self)->take(key, call);
}

//  void QGeoSatelliteInfoSource::setUpdateInterval(int msec)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QGeoSatelliteInfoSource17setUpdateIntervalEi(
    QGeoSatelliteInfoSource *self,
    int msec) {
  self->QGeoSatelliteInfoSource::setUpdateInterval(msec);
}

//  bool QGeoSatelliteInfoSource::setBackendProperty(const QString &name,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QGeoSatelliteInfoSource18setBackendPropertyERK7QStringRK8QVariant(
    QGeoSatelliteInfoSource *self,
    const QString *name,
    const QVariant *value) {
  return self->QGeoSatelliteInfoSource::setBackendProperty(*name, *value);
}

//  QVariant QGeoSatelliteInfoSource::backendProperty(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK23QGeoSatelliteInfoSource15backendPropertyERK7QString(
    const QGeoSatelliteInfoSource *self,
    const QString *name) {
  return new QVariant(self->QGeoSatelliteInfoSource::backendProperty(*name));
}
