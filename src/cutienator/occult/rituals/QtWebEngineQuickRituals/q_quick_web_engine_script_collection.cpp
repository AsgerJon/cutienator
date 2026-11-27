//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebenginescriptcollection_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginescriptcollection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtWebEngineCore/qwebenginescript.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickWebEngineScriptCollection that Python can take functions over in. Every QQuickWebEngineScriptCollection
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineScriptCollectionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineScriptCollectionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineScriptCollectionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineScriptCollectionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineScriptCollectionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineScriptCollectionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineScriptCollectionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWebEngineScriptCollection : public QQuickWebEngineScriptCollection {
public:
  using QQuickWebEngineScriptCollection::QQuickWebEngineScriptCollection;
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
      CuteQQuickWebEngineScriptCollectionCall0 call = reinterpret_cast<CuteQQuickWebEngineScriptCollectionCall0>(taken[0]);
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
      CuteQQuickWebEngineScriptCollectionCall1 call = reinterpret_cast<CuteQQuickWebEngineScriptCollectionCall1>(taken[1]);
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
      CuteQQuickWebEngineScriptCollectionCall2 call = reinterpret_cast<CuteQQuickWebEngineScriptCollectionCall2>(taken[2]);
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
      CuteQQuickWebEngineScriptCollectionCall3 call = reinterpret_cast<CuteQQuickWebEngineScriptCollectionCall3>(taken[3]);
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
      CuteQQuickWebEngineScriptCollectionCall4 call = reinterpret_cast<CuteQQuickWebEngineScriptCollectionCall4>(taken[4]);
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
      CuteQQuickWebEngineScriptCollectionCall5 call = reinterpret_cast<CuteQQuickWebEngineScriptCollectionCall5>(taken[5]);
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
      CuteQQuickWebEngineScriptCollectionCall6 call = reinterpret_cast<CuteQQuickWebEngineScriptCollectionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWebEngineScriptCollection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQuickWebEngineScriptCollection10metaObjectEv(
    const QQuickWebEngineScriptCollection *self) {
  return self->metaObject();
}

//  void *QQuickWebEngineScriptCollection::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QQuickWebEngineScriptCollection11qt_metacastEPKc(
    QQuickWebEngineScriptCollection *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWebEngineScriptCollection::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QQuickWebEngineScriptCollection11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebEngineScriptCollection *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebEngineScriptCollection::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QQuickWebEngineScriptCollection2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebEngineScriptCollection::tr(s, c, n));
}

//  void QQuickWebEngineScriptCollection::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineScriptCollection22qt_qmlMarker_anonymousEv(
    QQuickWebEngineScriptCollection *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickWebEngineScriptCollection::~QQuickWebEngineScriptCollection()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineScriptCollectionD1Ev(
    QQuickWebEngineScriptCollection *self) {
  delete self;
}

//  bool QQuickWebEngineScriptCollection::contains(const QWebEngineScript
//      &value) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQuickWebEngineScriptCollection8containsERK16QWebEngineScript(
    const QQuickWebEngineScriptCollection *self,
    const QWebEngineScript *value) {
  return self->contains(*value);
}

//  QList<QWebEngineScript> QQuickWebEngineScriptCollection::find(const
//      QString &name) const
extern "C" Q_DECL_EXPORT
QList<QWebEngineScript> *ritual_ZNK31QQuickWebEngineScriptCollection4findERK7QString(
    const QQuickWebEngineScriptCollection *self,
    const QString *name) {
  return new QList<QWebEngineScript>(self->find(*name));
}

//  void QQuickWebEngineScriptCollection::insert(const QWebEngineScript &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineScriptCollection6insertERK16QWebEngineScript(
    QQuickWebEngineScriptCollection *self,
    const QWebEngineScript *a0) {
  self->insert(*a0);
}

//  void QQuickWebEngineScriptCollection::insert(const
//      QList<QWebEngineScript> &list)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineScriptCollection6insertERK5QListI16QWebEngineScriptE(
    QQuickWebEngineScriptCollection *self,
    const QList<QWebEngineScript> *list) {
  self->insert(*list);
}

//  bool QQuickWebEngineScriptCollection::remove(const QWebEngineScript &a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QQuickWebEngineScriptCollection6removeERK16QWebEngineScript(
    QQuickWebEngineScriptCollection *self,
    const QWebEngineScript *a0) {
  return self->remove(*a0);
}

//  void QQuickWebEngineScriptCollection::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineScriptCollection5clearEv(
    QQuickWebEngineScriptCollection *self) {
  self->clear();
}

//  QList<QWebEngineScript> QQuickWebEngineScriptCollection::collection()
//      const
extern "C" Q_DECL_EXPORT
QList<QWebEngineScript> *ritual_ZNK31QQuickWebEngineScriptCollection10collectionEv(
    const QQuickWebEngineScriptCollection *self) {
  return new QList<QWebEngineScript>(self->collection());
}

//  void QQuickWebEngineScriptCollection::setCollection(const
//      QList<QWebEngineScript> &scripts)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineScriptCollection13setCollectionERK5QListI16QWebEngineScriptE(
    QQuickWebEngineScriptCollection *self,
    const QList<QWebEngineScript> *scripts) {
  self->setCollection(*scripts);
}

//  void QQuickWebEngineScriptCollection::collectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickWebEngineScriptCollection17collectionChangedEv(
    QQuickWebEngineScriptCollection *self) {
  self->collectionChanged();
}

//  QQuickWebEngineScriptCollection::QQuickWebEngineScriptCollection(QWebEngi
//      neScriptCollection *d)
extern "C" Q_DECL_EXPORT
QQuickWebEngineScriptCollection *ritual_ZN31QQuickWebEngineScriptCollectionC1EP26QWebEngineScriptCollection(
    QWebEngineScriptCollection *d) {
  return new CuteQQuickWebEngineScriptCollection(d);
}

//  a Python function taken by a CuteQQuickWebEngineScriptCollection, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWebEngineScriptCollection(
    QQuickWebEngineScriptCollection *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWebEngineScriptCollection *>(self)->take(key, call);
}
