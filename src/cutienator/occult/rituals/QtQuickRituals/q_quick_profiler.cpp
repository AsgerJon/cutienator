//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickprofiler_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, instances of templates of the class:
//  26. Kept as it is when the generator runs again.
#include <QtQml/qtqmlglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickprofiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qsize.h>
#include <QtCore/qelapsedtimer.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickProfiler that Python can take functions over in. Every QQuickProfiler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickProfilerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickProfilerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickProfilerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickProfilerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickProfilerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickProfilerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickProfilerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickProfiler : public QQuickProfiler {
public:
  using QQuickProfiler::QQuickProfiler;
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
      CuteQQuickProfilerCall0 call = reinterpret_cast<CuteQQuickProfilerCall0>(taken[0]);
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
      CuteQQuickProfilerCall1 call = reinterpret_cast<CuteQQuickProfilerCall1>(taken[1]);
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
      CuteQQuickProfilerCall2 call = reinterpret_cast<CuteQQuickProfilerCall2>(taken[2]);
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
      CuteQQuickProfilerCall3 call = reinterpret_cast<CuteQQuickProfilerCall3>(taken[3]);
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
      CuteQQuickProfilerCall4 call = reinterpret_cast<CuteQQuickProfilerCall4>(taken[4]);
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
      CuteQQuickProfilerCall5 call = reinterpret_cast<CuteQQuickProfilerCall5>(taken[5]);
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
      CuteQQuickProfilerCall6 call = reinterpret_cast<CuteQQuickProfilerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickProfiler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickProfiler10metaObjectEv(
    const QQuickProfiler *self) {
  return self->metaObject();
}

//  void *QQuickProfiler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickProfiler11qt_metacastEPKc(
    QQuickProfiler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickProfiler::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickProfiler11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickProfiler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickProfiler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickProfiler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickProfiler::tr(s, c, n));
}

//  void QQuickProfiler::animationFrame(qint64 delta, AnimationThread
//      threadId)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler14animationFrameExNS_15AnimationThreadE(
    qint64 delta,
    QQuickProfiler::AnimationThread threadId) {
  QQuickProfiler::animationFrame(delta, threadId);
}

//  void QQuickProfiler::pixmapLoadingFinished(const QUrl &url, const QSize
//      &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler21pixmapLoadingFinishedERK4QUrlRK5QSize(
    const QUrl *url,
    const QSize *size) {
  QQuickProfiler::pixmapLoadingFinished(*url, *size);
}

//  void QQuickProfiler::registerAnimationCallback()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler25registerAnimationCallbackEv() {
  QQuickProfiler::registerAnimationCallback();
}

//  qint64 QQuickProfiler::timestamp()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN14QQuickProfiler9timestampEv(QQuickProfiler *self) {
  return self->timestamp();
}

//  void QQuickProfiler::initialize(QObject *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler10initializeEP7QObject(QObject *parent) {
  QQuickProfiler::initialize(parent);
}

//  QQuickProfiler::~QQuickProfiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfilerD1Ev(QQuickProfiler *self) {
  delete self;
}

//  void QQuickProfiler::dataReady(const QList<QQuickProfilerData> &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler9dataReadyERK5QListI18QQuickProfilerDataE(
    QQuickProfiler *self,
    const QList<QQuickProfilerData> *data) {
  self->dataReady(*data);
}

//  QQuickProfiler::QQuickProfiler(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickProfiler *ritual_ZN14QQuickProfilerC1EP7QObject(QObject *parent) {
  return new CuteQQuickProfiler(parent);
}

//  void QQuickProfiler::processMessage(const QQuickProfilerData &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler14processMessageERK18QQuickProfilerData(
    QQuickProfiler *self,
    const QQuickProfilerData *message) {
  self->processMessage(*message);
}

//  void QQuickProfiler::startProfilingImpl(quint64 features)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler18startProfilingImplEy(
    QQuickProfiler *self,
    quint64 features) {
  self->startProfilingImpl(features);
}

//  void QQuickProfiler::stopProfilingImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler17stopProfilingImplEv(QQuickProfiler *self) {
  self->stopProfilingImpl();
}

//  void QQuickProfiler::reportDataImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler14reportDataImplEv(QQuickProfiler *self) {
  self->reportDataImpl();
}

//  void QQuickProfiler::setTimer(const QElapsedTimer &t)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler8setTimerERK13QElapsedTimer(
    QQuickProfiler *self,
    const QElapsedTimer *t) {
  self->setTimer(*t);
}

//  QQuickProfiler as the QQmlProfilerDefinitions it is built on
extern "C" Q_DECL_EXPORT
QQmlProfilerDefinitions *ritual_cast_QQuickProfiler_QQmlProfilerDefinitions(
    QQuickProfiler *self) {
  return static_cast<QQmlProfilerDefinitions *>(self);
}

//  a Python function taken by a CuteQQuickProfiler, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickProfiler(
    QQuickProfiler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickProfiler *>(self)->take(key, call);
}

//  static void QQuickProfiler::inputEvent<QQuickProfiler::Mouse,
//      QQuickProfiler::InputMousePress>(int x, int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler10inputEventILN23QQmlProfilerDefinitions9EventTypeE1ELNS1_14InputEventTypeE3EEEvii(
    int x,
    int y) {
  QQuickProfiler::inputEvent<QQuickProfiler::Mouse,
      QQuickProfiler::InputMousePress>(x, y);
}

//  static void QQuickProfiler::inputEvent<QQuickProfiler::Mouse,
//      QQuickProfiler::InputMouseRelease>(int x, int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler10inputEventILN23QQmlProfilerDefinitions9EventTypeE1ELNS1_14InputEventTypeE4EEEvii(
    int x,
    int y) {
  QQuickProfiler::inputEvent<QQuickProfiler::Mouse,
      QQuickProfiler::InputMouseRelease>(x, y);
}

//  static void QQuickProfiler::inputEvent<QQuickProfiler::Mouse,
//      QQuickProfiler::InputMouseWheel>(int x, int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler10inputEventILN23QQmlProfilerDefinitions9EventTypeE1ELNS1_14InputEventTypeE7EEEvii(
    int x,
    int y) {
  QQuickProfiler::inputEvent<QQuickProfiler::Mouse,
      QQuickProfiler::InputMouseWheel>(x, y);
}

//  static void QQuickProfiler::inputEvent<QQuickProfiler::Key,
//      QQuickProfiler::InputKeyPress>(int x, int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler10inputEventILN23QQmlProfilerDefinitions9EventTypeE2ELNS1_14InputEventTypeE0EEEvii(
    int x,
    int y) {
  QQuickProfiler::inputEvent<QQuickProfiler::Key,
      QQuickProfiler::InputKeyPress>(x, y);
}

//  static void QQuickProfiler::inputEvent<QQuickProfiler::Key,
//      QQuickProfiler::InputKeyRelease>(int x, int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler10inputEventILN23QQmlProfilerDefinitions9EventTypeE2ELNS1_14InputEventTypeE1EEEvii(
    int x,
    int y) {
  QQuickProfiler::inputEvent<QQuickProfiler::Key,
      QQuickProfiler::InputKeyRelease>(x, y);
}

//  static void
//      QQuickProfiler::startSceneGraphFrame<QQuickProfiler::SceneGraphRendererFrame>()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler20startSceneGraphFrameILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE0EEEvv(
    ) {
  QQuickProfiler::startSceneGraphFrame<QQuickProfiler::SceneGraphRendererFrame>();
}

//  static void
//      QQuickProfiler::startSceneGraphFrame<QQuickProfiler::SceneGraphAdaptationLayerFrame>()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler20startSceneGraphFrameILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE1EEEvv(
    ) {
  QQuickProfiler::startSceneGraphFrame<QQuickProfiler::SceneGraphAdaptationLayerFrame>();
}

//  static void
//      QQuickProfiler::startSceneGraphFrame<QQuickProfiler::SceneGraphRenderLoopFrame>()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler20startSceneGraphFrameILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE3EEEvv(
    ) {
  QQuickProfiler::startSceneGraphFrame<QQuickProfiler::SceneGraphRenderLoopFrame>();
}

//  static void
//      QQuickProfiler::startSceneGraphFrame<QQuickProfiler::SceneGraphPolishAndSync>()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler20startSceneGraphFrameILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE6EEEvv(
    ) {
  QQuickProfiler::startSceneGraphFrame<QQuickProfiler::SceneGraphPolishAndSync>();
}

//  static void
//      QQuickProfiler::startSceneGraphFrame<QQuickProfiler::SceneGraphPolishFrame>()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler20startSceneGraphFrameILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE9EEEvv(
    ) {
  QQuickProfiler::startSceneGraphFrame<QQuickProfiler::SceneGraphPolishFrame>();
}

//  static void
//      QQuickProfiler::recordSceneGraphTimestamp<QQuickProfiler::SceneGraphRendererFrame>(uint
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler25recordSceneGraphTimestampILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE0EEEvj(
    unsigned int position) {
  QQuickProfiler::recordSceneGraphTimestamp<
      QQuickProfiler::SceneGraphRendererFrame>(position);
}

//  static void
//      QQuickProfiler::recordSceneGraphTimestamp<QQuickProfiler::SceneGraphAdaptationLayerFrame>(uint
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler25recordSceneGraphTimestampILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE1EEEvj(
    unsigned int position) {
  QQuickProfiler::recordSceneGraphTimestamp<
      QQuickProfiler::SceneGraphAdaptationLayerFrame>(position);
}

//  static void
//      QQuickProfiler::recordSceneGraphTimestamp<QQuickProfiler::SceneGraphRenderLoopFrame>(uint
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler25recordSceneGraphTimestampILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE3EEEvj(
    unsigned int position) {
  QQuickProfiler::recordSceneGraphTimestamp<
      QQuickProfiler::SceneGraphRenderLoopFrame>(position);
}

//  static void
//      QQuickProfiler::recordSceneGraphTimestamp<QQuickProfiler::SceneGraphPolishAndSync>(uint
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler25recordSceneGraphTimestampILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE6EEEvj(
    unsigned int position) {
  QQuickProfiler::recordSceneGraphTimestamp<
      QQuickProfiler::SceneGraphPolishAndSync>(position);
}

//  static void
//      QQuickProfiler::recordSceneGraphTimestamp<QQuickProfiler::SceneGraphPolishFrame>(uint
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler25recordSceneGraphTimestampILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE9EEEvj(
    unsigned int position) {
  QQuickProfiler::recordSceneGraphTimestamp<
      QQuickProfiler::SceneGraphPolishFrame>(position);
}

//  static void
//      QQuickProfiler::skipSceneGraphTimestamps<QQuickProfiler::SceneGraphRenderLoopFrame,
//      1>(uint position)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler24skipSceneGraphTimestampsILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE3ELj1EEEvj(
    unsigned int position) {
  QQuickProfiler::skipSceneGraphTimestamps<
      QQuickProfiler::SceneGraphRenderLoopFrame, 1>(position);
}

//  static void
//      QQuickProfiler::reportSceneGraphFrame<QQuickProfiler::SceneGraphRenderLoopFrame,
//      true>(uint position, quint64 payload)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler21reportSceneGraphFrameILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE3ELb1EEEvjy(
    unsigned int position,
    long long payload) {
  QQuickProfiler::reportSceneGraphFrame<
      QQuickProfiler::SceneGraphRenderLoopFrame, true>(
      position, static_cast<quint64>(payload));
}

//  static void
//      QQuickProfiler::reportSceneGraphFrame<QQuickProfiler::SceneGraphRenderLoopFrame,
//      false>(uint position, quint64 payload)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler21reportSceneGraphFrameILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE3ELb0EEEvjy(
    unsigned int position,
    long long payload) {
  QQuickProfiler::reportSceneGraphFrame<
      QQuickProfiler::SceneGraphRenderLoopFrame, false>(
      position, static_cast<quint64>(payload));
}

//  static void
//      QQuickProfiler::reportSceneGraphFrame<QQuickProfiler::SceneGraphRendererFrame,
//      true>(uint position, quint64 payload)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler21reportSceneGraphFrameILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE0ELb1EEEvjy(
    unsigned int position,
    long long payload) {
  QQuickProfiler::reportSceneGraphFrame<
      QQuickProfiler::SceneGraphRendererFrame, true>(
      position, static_cast<quint64>(payload));
}

//  static void
//      QQuickProfiler::reportSceneGraphFrame<QQuickProfiler::SceneGraphPolishAndSync,
//      true>(uint position, quint64 payload)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler21reportSceneGraphFrameILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE6ELb1EEEvjy(
    unsigned int position,
    long long payload) {
  QQuickProfiler::reportSceneGraphFrame<
      QQuickProfiler::SceneGraphPolishAndSync, true>(
      position, static_cast<quint64>(payload));
}

//  static void
//      QQuickProfiler::reportSceneGraphFrame<QQuickProfiler::SceneGraphPolishFrame,
//      true>(uint position, quint64 payload)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler21reportSceneGraphFrameILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE9ELb1EEEvjy(
    unsigned int position,
    long long payload) {
  QQuickProfiler::reportSceneGraphFrame<
      QQuickProfiler::SceneGraphPolishFrame, true>(
      position, static_cast<quint64>(payload));
}

//  static void
//      QQuickProfiler::reportSceneGraphFrame<QQuickProfiler::SceneGraphPolishFrame,
//      true, QQuickProfiler::SceneGraphRenderLoopFrame>(uint position,
//      quint64 payload)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler21reportSceneGraphFrameILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE9ELb1ELS2_3EEEvjy(
    unsigned int position,
    long long payload) {
  QQuickProfiler::reportSceneGraphFrame<
      QQuickProfiler::SceneGraphPolishFrame, true,
      QQuickProfiler::SceneGraphRenderLoopFrame>(
      position, static_cast<quint64>(payload));
}

//  static void
//      QQuickProfiler::pixmapStateChanged<QQuickProfiler::PixmapLoadingStarted>(const
//      QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler18pixmapStateChangedILN23QQmlProfilerDefinitions15PixmapEventTypeE3EEEvRK4QUrl(
    const QUrl *url) {
  QQuickProfiler::pixmapStateChanged<QQuickProfiler::PixmapLoadingStarted>(*url);
}

//  static void
//      QQuickProfiler::pixmapStateChanged<QQuickProfiler::PixmapLoadingError>(const
//      QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler18pixmapStateChangedILN23QQmlProfilerDefinitions15PixmapEventTypeE5EEEvRK4QUrl(
    const QUrl *url) {
  QQuickProfiler::pixmapStateChanged<QQuickProfiler::PixmapLoadingError>(*url);
}

//  static void
//      QQuickProfiler::pixmapCountChanged<QQuickProfiler::PixmapReferenceCountChanged>(const
//      QUrl &url, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler18pixmapCountChangedILN23QQmlProfilerDefinitions15PixmapEventTypeE1EEEvRK4QUrli(
    const QUrl *url,
    int count) {
  QQuickProfiler::pixmapCountChanged<QQuickProfiler::PixmapReferenceCountChanged>(*url, count);
}

//  static void
//      QQuickProfiler::pixmapCountChanged<QQuickProfiler::PixmapCacheCountChanged>(const
//      QUrl &url, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler18pixmapCountChangedILN23QQmlProfilerDefinitions15PixmapEventTypeE2EEEvRK4QUrli(
    const QUrl *url,
    int count) {
  QQuickProfiler::pixmapCountChanged<QQuickProfiler::PixmapCacheCountChanged>(*url, count);
}

#endif  // !(!QT_CONFIG(qml_debug))
