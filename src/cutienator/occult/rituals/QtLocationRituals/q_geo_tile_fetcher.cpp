//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeotilefetcher_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotilefetcher_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotilespec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QGeoTileFetcher may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGeoTileFetcher : QGeoTileFetcher {
  using QGeoTileFetcher::timerEvent;
  using QGeoTileFetcher::initialized;
  using QGeoTileFetcher::fetchingEnabled;
};

//  A QGeoTileFetcher that Python can take functions over in. Every QGeoTileFetcher
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTileFetcherCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoTileFetcherCall1)(const void *, int *);
typedef bool (*CuteQGeoTileFetcherCall2)(const void *, int *);
typedef void * (*CuteQGeoTileFetcherCall3)(const void *, const QGeoTileSpec *, int *);
typedef void (*CuteQGeoTileFetcherCall4)(const void *, QGeoTiledMapReply *, const QGeoTileSpec *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoTileFetcherCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoTileFetcherCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTileFetcherCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTileFetcherCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTileFetcherCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTileFetcherCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoTileFetcher : public QGeoTileFetcher {
public:
  using QGeoTileFetcher::QGeoTileFetcher;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK15QGeoTileFetcher11initializedEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QGeoTileFetcher15fetchingEnabledEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGeoTileFetcher12getTileImageERK12QGeoTileSpec")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGeoTileFetcher11handleReplyEP17QGeoTiledMapReplyRK12QGeoTileSpec")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  void QGeoTileFetcher::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoTileFetcherCall0 call = reinterpret_cast<CuteQGeoTileFetcherCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGeoTileFetcher::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  bool QGeoTileFetcher::initialized() const
  bool initialized() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoTileFetcherCall1 call = reinterpret_cast<CuteQGeoTileFetcherCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoTileFetcher::initialized();
  }

  //  bool QGeoTileFetcher::fetchingEnabled() const
  bool fetchingEnabled() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoTileFetcherCall2 call = reinterpret_cast<CuteQGeoTileFetcherCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoTileFetcher::fetchingEnabled();
  }

  //  QGeoTiledMapReply *QGeoTileFetcher::getTileImage(const QGeoTileSpec
  //      &spec)
  QGeoTiledMapReply *getTileImage(const QGeoTileSpec &spec) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoTileFetcherCall3 call = reinterpret_cast<CuteQGeoTileFetcherCall3>(taken[3]);
      void * given = call(this, &spec, &handled);
      if (handled) return static_cast<QGeoTiledMapReply *>(given);
    }
    return {};
  }

  //  void QGeoTileFetcher::handleReply(QGeoTiledMapReply *reply, const
  //      QGeoTileSpec &spec)
  void handleReply(
      QGeoTiledMapReply *reply,
      const QGeoTileSpec &spec) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoTileFetcherCall4 call = reinterpret_cast<CuteQGeoTileFetcherCall4>(taken[4]);
      call(this, reply, &spec, &handled);
      if (handled) return;
    }
    QGeoTileFetcher::handleReply(reply, spec);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoTileFetcherCall5 call = reinterpret_cast<CuteQGeoTileFetcherCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoTileFetcherCall6 call = reinterpret_cast<CuteQGeoTileFetcherCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGeoTileFetcherCall7 call = reinterpret_cast<CuteQGeoTileFetcherCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGeoTileFetcherCall8 call = reinterpret_cast<CuteQGeoTileFetcherCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGeoTileFetcherCall9 call = reinterpret_cast<CuteQGeoTileFetcherCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQGeoTileFetcherCall10 call = reinterpret_cast<CuteQGeoTileFetcherCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoTileFetcher::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QGeoTileFetcher10metaObjectEv(
    const QGeoTileFetcher *self) {
  return self->metaObject();
}

//  void *QGeoTileFetcher::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QGeoTileFetcher11qt_metacastEPKc(
    QGeoTileFetcher *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGeoTileFetcher::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QGeoTileFetcher11qt_metacallEN11QMetaObject4CallEiPPv(
    QGeoTileFetcher *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGeoTileFetcher::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGeoTileFetcher2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoTileFetcher::tr(s, c, n));
}

//  QGeoTileFetcherPrivate *QGeoTileFetcher::d_func()
extern "C" Q_DECL_EXPORT
QGeoTileFetcherPrivate *ritual_ZN15QGeoTileFetcher6d_funcEv(
    QGeoTileFetcher *self) {
  return self->d_func();
}

//  const QGeoTileFetcherPrivate *QGeoTileFetcher::d_func() const
extern "C" Q_DECL_EXPORT
const QGeoTileFetcherPrivate *ritual_ZNK15QGeoTileFetcher6d_funcEv(
    const QGeoTileFetcher *self) {
  return self->d_func();
}

//  QGeoTileFetcher::QGeoTileFetcher(QGeoMappingManagerEngine *parent)
extern "C" Q_DECL_EXPORT
QGeoTileFetcher *ritual_ZN15QGeoTileFetcherC1EP24QGeoMappingManagerEngine(
    QGeoMappingManagerEngine *parent) {
  return new CuteQGeoTileFetcher(parent);
}

//  QGeoTileFetcher::~QGeoTileFetcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoTileFetcherD1Ev(QGeoTileFetcher *self) {
  delete self;
}

//  void QGeoTileFetcher::updateTileRequests(const QSet<QGeoTileSpec>
//      &tilesAdded, const QSet<QGeoTileSpec> &tilesRemoved)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoTileFetcher18updateTileRequestsERK4QSetI12QGeoTileSpecES4_(
    QGeoTileFetcher *self,
    const QSet<QGeoTileSpec> *tilesAdded,
    const QSet<QGeoTileSpec> *tilesRemoved) {
  self->updateTileRequests(*tilesAdded, *tilesRemoved);
}

//  void QGeoTileFetcher::cancelTileRequests(const QSet<QGeoTileSpec> &tiles)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoTileFetcher18cancelTileRequestsERK4QSetI12QGeoTileSpecE(
    QGeoTileFetcher *self,
    const QSet<QGeoTileSpec> *tiles) {
  self->cancelTileRequests(*tiles);
}

//  void QGeoTileFetcher::requestNextTile()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoTileFetcher15requestNextTileEv(QGeoTileFetcher *self) {
  self->requestNextTile();
}

//  void QGeoTileFetcher::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoTileFetcher8finishedEv(QGeoTileFetcher *self) {
  self->finished();
}

//  void QGeoTileFetcher::tileFinished(const QGeoTileSpec &spec, const
//      QByteArray &bytes, const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoTileFetcher12tileFinishedERK12QGeoTileSpecRK10QByteArrayRK7QString(
    QGeoTileFetcher *self,
    const QGeoTileSpec *spec,
    const QByteArray *bytes,
    const QString *format) {
  self->tileFinished(*spec, *bytes, *format);
}

//  void QGeoTileFetcher::tileError(const QGeoTileSpec &spec, const QString
//      &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoTileFetcher9tileErrorERK12QGeoTileSpecRK7QString(
    QGeoTileFetcher *self,
    const QGeoTileSpec *spec,
    const QString *errorString) {
  self->tileError(*spec, *errorString);
}

//  QGeoTileFetcher::QGeoTileFetcher(QGeoTileFetcherPrivate &dd,
//      QGeoMappingManagerEngine *parent)
extern "C" Q_DECL_EXPORT
QGeoTileFetcher *ritual_ZN15QGeoTileFetcherC1ER22QGeoTileFetcherPrivateP24QGeoMappingManagerEngine(
    QGeoTileFetcherPrivate *dd,
    QGeoMappingManagerEngine *parent) {
  return new CuteQGeoTileFetcher(*dd, parent);
}

//  void QGeoTileFetcher::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoTileFetcher10timerEventEP11QTimerEvent(
    QGeoTileFetcher *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  bool QGeoTileFetcher::initialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGeoTileFetcher11initializedEv(
    const QGeoTileFetcher *self) {
  return self->initialized();
}

//  bool QGeoTileFetcher::fetchingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGeoTileFetcher15fetchingEnabledEv(
    const QGeoTileFetcher *self) {
  return self->fetchingEnabled();
}

//  QGeoTiledMapReply *QGeoTileFetcher::getTileImage(const QGeoTileSpec
//      &spec)
extern "C" Q_DECL_EXPORT
QGeoTiledMapReply *ritual_ZN15QGeoTileFetcher12getTileImageERK12QGeoTileSpec(
    QGeoTileFetcher *self,
    const QGeoTileSpec *spec) {
  return self->getTileImage(*spec);
}

//  void QGeoTileFetcher::handleReply(QGeoTiledMapReply *reply, const
//      QGeoTileSpec &spec)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoTileFetcher11handleReplyEP17QGeoTiledMapReplyRK12QGeoTileSpec(
    QGeoTileFetcher *self,
    QGeoTiledMapReply *reply,
    const QGeoTileSpec *spec) {
  self->handleReply(reply, *spec);
}

//  a Python function taken by a CuteQGeoTileFetcher, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoTileFetcher(
    QGeoTileFetcher *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoTileFetcher *>(self)->take(key, call);
}

//  void QGeoTileFetcher::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGeoTileFetcher10timerEventEP11QTimerEvent(
    QGeoTileFetcher *self,
    QTimerEvent *event) {
  static_cast<OwnQGeoTileFetcher *>(self)->OwnQGeoTileFetcher::timerEvent(
      event);
}

//  bool QGeoTileFetcher::initialized() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QGeoTileFetcher11initializedEv(
    const QGeoTileFetcher *self) {
  return static_cast<const OwnQGeoTileFetcher *>(self)->OwnQGeoTileFetcher::initialized();
}

//  bool QGeoTileFetcher::fetchingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QGeoTileFetcher15fetchingEnabledEv(
    const QGeoTileFetcher *self) {
  return static_cast<const OwnQGeoTileFetcher *>(self)->OwnQGeoTileFetcher::fetchingEnabled();
}

//  void QGeoTileFetcher::handleReply(QGeoTiledMapReply *reply, const
//      QGeoTileSpec &spec)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGeoTileFetcher11handleReplyEP17QGeoTiledMapReplyRK12QGeoTileSpec(
    QGeoTileFetcher *self,
    QGeoTiledMapReply *reply,
    const QGeoTileSpec *spec) {
  self->QGeoTileFetcher::handleReply(reply, *spec);
}
