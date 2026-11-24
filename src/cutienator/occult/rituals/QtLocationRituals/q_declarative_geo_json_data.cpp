//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativegeojsondata_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeojsondata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDeclarativeGeoJsonData that Python can take functions over in. Every QDeclarativeGeoJsonData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoJsonDataCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoJsonDataCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoJsonDataCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoJsonDataCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoJsonDataCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoJsonDataCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoJsonDataCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeGeoJsonData : public QDeclarativeGeoJsonData {
public:
  using QDeclarativeGeoJsonData::QDeclarativeGeoJsonData;
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
      CuteQDeclarativeGeoJsonDataCall0 call = reinterpret_cast<CuteQDeclarativeGeoJsonDataCall0>(taken[0]);
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
      CuteQDeclarativeGeoJsonDataCall1 call = reinterpret_cast<CuteQDeclarativeGeoJsonDataCall1>(taken[1]);
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
      CuteQDeclarativeGeoJsonDataCall2 call = reinterpret_cast<CuteQDeclarativeGeoJsonDataCall2>(taken[2]);
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
      CuteQDeclarativeGeoJsonDataCall3 call = reinterpret_cast<CuteQDeclarativeGeoJsonDataCall3>(taken[3]);
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
      CuteQDeclarativeGeoJsonDataCall4 call = reinterpret_cast<CuteQDeclarativeGeoJsonDataCall4>(taken[4]);
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
      CuteQDeclarativeGeoJsonDataCall5 call = reinterpret_cast<CuteQDeclarativeGeoJsonDataCall5>(taken[5]);
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
      CuteQDeclarativeGeoJsonDataCall6 call = reinterpret_cast<CuteQDeclarativeGeoJsonDataCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeGeoJsonData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QDeclarativeGeoJsonData10metaObjectEv(
    const QDeclarativeGeoJsonData *self) {
  return self->metaObject();
}

//  QString QDeclarativeGeoJsonData::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QDeclarativeGeoJsonData2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeGeoJsonData::tr(s, c, n));
}

//  QDeclarativeGeoJsonData::QDeclarativeGeoJsonData(QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoJsonData *ritual_ZN23QDeclarativeGeoJsonDataC1EP7QObject(
    QObject *parent) {
  return new CuteQDeclarativeGeoJsonData(parent);
}

//  QDeclarativeGeoJsonData::~QDeclarativeGeoJsonData()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDeclarativeGeoJsonDataD1Ev(QDeclarativeGeoJsonData *self) {
  delete self;
}

//  QVariant QDeclarativeGeoJsonData::model() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QDeclarativeGeoJsonData5modelEv(
    const QDeclarativeGeoJsonData *self) {
  return new QVariant(self->model());
}

//  void QDeclarativeGeoJsonData::setModel(const QVariant &model)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDeclarativeGeoJsonData8setModelERK8QVariant(
    QDeclarativeGeoJsonData *self,
    const QVariant *model) {
  self->setModel(*model);
}

//  QUrl QDeclarativeGeoJsonData::sourceUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK23QDeclarativeGeoJsonData9sourceUrlEv(
    const QDeclarativeGeoJsonData *self) {
  return new QUrl(self->sourceUrl());
}

//  void QDeclarativeGeoJsonData::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDeclarativeGeoJsonData5clearEv(
    QDeclarativeGeoJsonData *self) {
  self->clear();
}

//  void QDeclarativeGeoJsonData::addItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDeclarativeGeoJsonData7addItemEP10QQuickItem(
    QDeclarativeGeoJsonData *self,
    QQuickItem *item) {
  self->addItem(item);
}

//  bool QDeclarativeGeoJsonData::open()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QDeclarativeGeoJsonData4openEv(
    QDeclarativeGeoJsonData *self) {
  return self->open();
}

//  bool QDeclarativeGeoJsonData::openUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QDeclarativeGeoJsonData7openUrlERK4QUrl(
    QDeclarativeGeoJsonData *self,
    const QUrl *url) {
  return self->openUrl(*url);
}

//  bool QDeclarativeGeoJsonData::save()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QDeclarativeGeoJsonData4saveEv(
    QDeclarativeGeoJsonData *self) {
  return self->save();
}

//  bool QDeclarativeGeoJsonData::saveAs(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QDeclarativeGeoJsonData6saveAsERK4QUrl(
    QDeclarativeGeoJsonData *self,
    const QUrl *url) {
  return self->saveAs(*url);
}

//  void QDeclarativeGeoJsonData::setModelToMapContents(QDeclarativeGeoMap
//      *map)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDeclarativeGeoJsonData21setModelToMapContentsEP18QDeclarativeGeoMap(
    QDeclarativeGeoJsonData *self,
    QDeclarativeGeoMap *map) {
  self->setModelToMapContents(map);
}

//  QVariantList QDeclarativeGeoJsonData::toVariant(QDeclarativeGeoMap
//      *mapItemView)
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZN23QDeclarativeGeoJsonData9toVariantEP18QDeclarativeGeoMap(
    QDeclarativeGeoMap *mapItemView) {
  return new QList<QVariant>(
      QDeclarativeGeoJsonData::toVariant(
          mapItemView));
}

//  bool QDeclarativeGeoJsonData::dumpGeoJSON(const QVariantList &geoJson,
//      const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QDeclarativeGeoJsonData11dumpGeoJSONERK5QListI8QVariantERK4QUrl(
    const QList<QVariant> *geoJson,
    const QUrl *url) {
  return QDeclarativeGeoJsonData::dumpGeoJSON(*geoJson, *url);
}

//  bool QDeclarativeGeoJsonData::writeDebug(const QVariantList &geoJson,
//      const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QDeclarativeGeoJsonData10writeDebugERK5QListI8QVariantERK4QUrl(
    const QList<QVariant> *geoJson,
    const QUrl *url) {
  return QDeclarativeGeoJsonData::writeDebug(*geoJson, *url);
}

//  QString QDeclarativeGeoJsonData::toString(const QVariantList &geoJson)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QDeclarativeGeoJsonData8toStringERK5QListI8QVariantE(
    const QList<QVariant> *geoJson) {
  return new QString(QDeclarativeGeoJsonData::toString(*geoJson));
}

//  a Python function taken by a CuteQDeclarativeGeoJsonData, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeGeoJsonData(
    QDeclarativeGeoJsonData *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeGeoJsonData *>(self)->take(key, call);
}
