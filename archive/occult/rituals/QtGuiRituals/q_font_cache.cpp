//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfont_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/QtGui>
#include <QtGui/6.12.0/QtGui/private/qfont_p.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QFontCache that Python can take functions over in. Every QFontCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQFontCacheCall0)(const void *, QTimerEvent *, int *);
typedef bool (*CuteQFontCacheCall1)(const void *, QEvent *, int *);
typedef bool (*CuteQFontCacheCall2)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQFontCacheCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQFontCacheCall4)(const void *, QEvent *, int *);
typedef void (*CuteQFontCacheCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQFontCacheCall6)(const void *, const QMetaMethod *, int *);
class CuteQFontCache : public QFontCache {
public:
  using QFontCache::QFontCache;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  void QFontCache::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQFontCacheCall0 call = reinterpret_cast<CuteQFontCacheCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QFontCache::timerEvent(event);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFontCacheCall1 call = reinterpret_cast<CuteQFontCacheCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFontCacheCall2 call = reinterpret_cast<CuteQFontCacheCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFontCacheCall3 call = reinterpret_cast<CuteQFontCacheCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQFontCacheCall4 call = reinterpret_cast<CuteQFontCacheCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQFontCacheCall5 call = reinterpret_cast<CuteQFontCacheCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQFontCacheCall6 call = reinterpret_cast<CuteQFontCacheCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  QFontCache *QFontCache::instance()
extern "C" Q_DECL_EXPORT
QFontCache *ritual_ZN10QFontCache8instanceEv() {
  return QFontCache::instance();
}

//  void QFontCache::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QFontCache7cleanupEv() {
  QFontCache::cleanup();
}

//  QFontCache::QFontCache()
extern "C" Q_DECL_EXPORT
QFontCache *ritual_ZN10QFontCacheC1Ev() {
  return new CuteQFontCache();
}

//  QFontCache::~QFontCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QFontCacheD1Ev(QFontCache *self) {
  delete self;
}

//  int QFontCache::id() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QFontCache2idEv(const QFontCache *self) {
  return self->id();
}

//  void QFontCache::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QFontCache5clearEv(QFontCache *self) {
  self->clear();
}

//  void QFontCache::increaseCost(uint cost)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QFontCache12increaseCostEj(QFontCache *self, uint cost) {
  self->increaseCost(cost);
}

//  void QFontCache::decreaseCost(uint cost)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QFontCache12decreaseCostEj(QFontCache *self, uint cost) {
  self->decreaseCost(cost);
}

//  void QFontCache::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QFontCache10timerEventEP11QTimerEvent(
    QFontCache *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QFontCache::decreaseCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QFontCache13decreaseCacheEv(QFontCache *self) {
  self->decreaseCache();
}

//  a Python function taken by a CuteQFontCache, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFontCache(QFontCache *self, const char *key, void *call) {
  return static_cast<CuteQFontCache *>(self)->take(key, call);
}

//  void QFontCache::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QFontCache10timerEventEP11QTimerEvent(
    QFontCache *self,
    QTimerEvent *event) {
  self->QFontCache::timerEvent(event);
}
