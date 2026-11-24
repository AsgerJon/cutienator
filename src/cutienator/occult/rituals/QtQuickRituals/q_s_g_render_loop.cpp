//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrenderloop_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrenderloop_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGRenderLoop that Python can take functions over in. Every QSGRenderLoop
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGRenderLoopCall0)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGRenderLoopCall1)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGRenderLoopCall2)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGRenderLoopCall3)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGRenderLoopCall4)(const void *, QQuickWindow *, int *);
typedef const QImage * (*CuteQSGRenderLoopCall5)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGRenderLoopCall6)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGRenderLoopCall7)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGRenderLoopCall8)(const void *, QQuickWindow *, int *);
typedef void * (*CuteQSGRenderLoopCall9)(const void *, int *);
typedef void * (*CuteQSGRenderLoopCall10)(const void *, int *);
typedef void * (*CuteQSGRenderLoopCall11)(const void *, QSGContext *, int *);
typedef void (*CuteQSGRenderLoopCall12)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGRenderLoopCall13)(const void *, QQuickWindow *, QRunnable *, int *);
typedef int (*CuteQSGRenderLoopCall14)(const void *, int *);
typedef bool (*CuteQSGRenderLoopCall15)(const void *, int *);
typedef int (*CuteQSGRenderLoopCall16)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRenderLoopCall17)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRenderLoopCall18)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRenderLoopCall19)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRenderLoopCall20)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRenderLoopCall21)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRenderLoopCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRenderLoopCall23)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGRenderLoop : public QSGRenderLoop {
public:
  using QSGRenderLoop::QSGRenderLoop;
  void *taken[24] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QSGRenderLoop4showEP12QQuickWindow")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop4hideEP12QQuickWindow")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop6resizeEP12QQuickWindow")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop15windowDestroyedEP12QQuickWindow")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop15exposureChangedEP12QQuickWindow")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop4grabEP12QQuickWindow")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop6updateEP12QQuickWindow")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop11maybeUpdateEP12QQuickWindow")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop19handleUpdateRequestEP12QQuickWindow")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop15animationDriverEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop17sceneGraphContextEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop19createRenderContextEP10QSGContext")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop16releaseResourcesEP12QQuickWindow")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop7postJobEP12QQuickWindowP9QRunnable")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop17windowSurfaceTypeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop20interleaveIncubationEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop5flagsEv")) {
      taken[16] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QSGRenderLoop::show(QQuickWindow *window)
  void show(QQuickWindow *window) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRenderLoopCall0 call = reinterpret_cast<CuteQSGRenderLoopCall0>(taken[0]);
      call(this, window, &handled);
      if (handled) return;
    }
  }

  //  void QSGRenderLoop::hide(QQuickWindow *window)
  void hide(QQuickWindow *window) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRenderLoopCall1 call = reinterpret_cast<CuteQSGRenderLoopCall1>(taken[1]);
      call(this, window, &handled);
      if (handled) return;
    }
  }

  //  void QSGRenderLoop::resize(QQuickWindow *a0)
  void resize(QQuickWindow *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGRenderLoopCall2 call = reinterpret_cast<CuteQSGRenderLoopCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGRenderLoop::resize(a0);
  }

  //  void QSGRenderLoop::windowDestroyed(QQuickWindow *window)
  void windowDestroyed(QQuickWindow *window) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGRenderLoopCall3 call = reinterpret_cast<CuteQSGRenderLoopCall3>(taken[3]);
      call(this, window, &handled);
      if (handled) return;
    }
  }

  //  void QSGRenderLoop::exposureChanged(QQuickWindow *window)
  void exposureChanged(QQuickWindow *window) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGRenderLoopCall4 call = reinterpret_cast<CuteQSGRenderLoopCall4>(taken[4]);
      call(this, window, &handled);
      if (handled) return;
    }
  }

  //  QImage QSGRenderLoop::grab(QQuickWindow *window)
  QImage grab(QQuickWindow *window) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGRenderLoopCall5 call = reinterpret_cast<CuteQSGRenderLoopCall5>(taken[5]);
      const QImage * given = call(this, window, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QSGRenderLoop::update(QQuickWindow *window)
  void update(QQuickWindow *window) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGRenderLoopCall6 call = reinterpret_cast<CuteQSGRenderLoopCall6>(taken[6]);
      call(this, window, &handled);
      if (handled) return;
    }
  }

  //  void QSGRenderLoop::maybeUpdate(QQuickWindow *window)
  void maybeUpdate(QQuickWindow *window) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGRenderLoopCall7 call = reinterpret_cast<CuteQSGRenderLoopCall7>(taken[7]);
      call(this, window, &handled);
      if (handled) return;
    }
  }

  //  void QSGRenderLoop::handleUpdateRequest(QQuickWindow *a0)
  void handleUpdateRequest(QQuickWindow *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGRenderLoopCall8 call = reinterpret_cast<CuteQSGRenderLoopCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGRenderLoop::handleUpdateRequest(a0);
  }

  //  QAnimationDriver *QSGRenderLoop::animationDriver() const
  QAnimationDriver *animationDriver() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGRenderLoopCall9 call = reinterpret_cast<CuteQSGRenderLoopCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAnimationDriver *>(given);
    }
    return {};
  }

  //  QSGContext *QSGRenderLoop::sceneGraphContext() const
  QSGContext *sceneGraphContext() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGRenderLoopCall10 call = reinterpret_cast<CuteQSGRenderLoopCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGContext *>(given);
    }
    return {};
  }

  //  QSGRenderContext *QSGRenderLoop::createRenderContext(QSGContext *a0)
  //      const
  QSGRenderContext *createRenderContext(QSGContext *a0) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGRenderLoopCall11 call = reinterpret_cast<CuteQSGRenderLoopCall11>(taken[11]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QSGRenderContext *>(given);
    }
    return {};
  }

  //  void QSGRenderLoop::releaseResources(QQuickWindow *window)
  void releaseResources(QQuickWindow *window) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGRenderLoopCall12 call = reinterpret_cast<CuteQSGRenderLoopCall12>(taken[12]);
      call(this, window, &handled);
      if (handled) return;
    }
  }

  //  void QSGRenderLoop::postJob(QQuickWindow *window, QRunnable *job)
  void postJob(QQuickWindow *window, QRunnable *job) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGRenderLoopCall13 call = reinterpret_cast<CuteQSGRenderLoopCall13>(taken[13]);
      call(this, window, job, &handled);
      if (handled) return;
    }
    QSGRenderLoop::postJob(window, job);
  }

  //  QSurface::SurfaceType QSGRenderLoop::windowSurfaceType() const
  QSurface::SurfaceType windowSurfaceType() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGRenderLoopCall14 call = reinterpret_cast<CuteQSGRenderLoopCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QSGRenderLoop::windowSurfaceType();
  }

  //  bool QSGRenderLoop::interleaveIncubation() const
  bool interleaveIncubation() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGRenderLoopCall15 call = reinterpret_cast<CuteQSGRenderLoopCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRenderLoop::interleaveIncubation();
  }

  //  int QSGRenderLoop::flags() const
  int flags() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGRenderLoopCall16 call = reinterpret_cast<CuteQSGRenderLoopCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRenderLoop::flags();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGRenderLoopCall17 call = reinterpret_cast<CuteQSGRenderLoopCall17>(taken[17]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGRenderLoopCall18 call = reinterpret_cast<CuteQSGRenderLoopCall18>(taken[18]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGRenderLoopCall19 call = reinterpret_cast<CuteQSGRenderLoopCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGRenderLoopCall20 call = reinterpret_cast<CuteQSGRenderLoopCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSGRenderLoopCall21 call = reinterpret_cast<CuteQSGRenderLoopCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSGRenderLoopCall22 call = reinterpret_cast<CuteQSGRenderLoopCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSGRenderLoopCall23 call = reinterpret_cast<CuteQSGRenderLoopCall23>(taken[23]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGRenderLoop::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QSGRenderLoop10metaObjectEv(
    const QSGRenderLoop *self) {
  return self->metaObject();
}

//  QString QSGRenderLoop::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QSGRenderLoop2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGRenderLoop::tr(s, c, n));
}

//  QSGRenderLoop::~QSGRenderLoop()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderLoopD1Ev(QSGRenderLoop *self) {
  delete self;
}

//  void QSGRenderLoop::show(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderLoop4showEP12QQuickWindow(
    QSGRenderLoop *self,
    QQuickWindow *window) {
  self->show(window);
}

//  void QSGRenderLoop::hide(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderLoop4hideEP12QQuickWindow(
    QSGRenderLoop *self,
    QQuickWindow *window) {
  self->hide(window);
}

//  void QSGRenderLoop::resize(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderLoop6resizeEP12QQuickWindow(
    QSGRenderLoop *self,
    QQuickWindow *a0) {
  self->resize(a0);
}

//  void QSGRenderLoop::windowDestroyed(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderLoop15windowDestroyedEP12QQuickWindow(
    QSGRenderLoop *self,
    QQuickWindow *window) {
  self->windowDestroyed(window);
}

//  void QSGRenderLoop::exposureChanged(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderLoop15exposureChangedEP12QQuickWindow(
    QSGRenderLoop *self,
    QQuickWindow *window) {
  self->exposureChanged(window);
}

//  QImage QSGRenderLoop::grab(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN13QSGRenderLoop4grabEP12QQuickWindow(
    QSGRenderLoop *self,
    QQuickWindow *window) {
  return new QImage(self->grab(window));
}

//  void QSGRenderLoop::update(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderLoop6updateEP12QQuickWindow(
    QSGRenderLoop *self,
    QQuickWindow *window) {
  self->update(window);
}

//  void QSGRenderLoop::maybeUpdate(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderLoop11maybeUpdateEP12QQuickWindow(
    QSGRenderLoop *self,
    QQuickWindow *window) {
  self->maybeUpdate(window);
}

//  void QSGRenderLoop::handleUpdateRequest(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderLoop19handleUpdateRequestEP12QQuickWindow(
    QSGRenderLoop *self,
    QQuickWindow *a0) {
  self->handleUpdateRequest(a0);
}

//  QAnimationDriver *QSGRenderLoop::animationDriver() const
extern "C" Q_DECL_EXPORT
QAnimationDriver *ritual_ZNK13QSGRenderLoop15animationDriverEv(
    const QSGRenderLoop *self) {
  return self->animationDriver();
}

//  QSGContext *QSGRenderLoop::sceneGraphContext() const
extern "C" Q_DECL_EXPORT
QSGContext *ritual_ZNK13QSGRenderLoop17sceneGraphContextEv(
    const QSGRenderLoop *self) {
  return self->sceneGraphContext();
}

//  QSGRenderContext *QSGRenderLoop::createRenderContext(QSGContext *a0)
//      const
extern "C" Q_DECL_EXPORT
QSGRenderContext *ritual_ZNK13QSGRenderLoop19createRenderContextEP10QSGContext(
    const QSGRenderLoop *self,
    QSGContext *a0) {
  return self->createRenderContext(a0);
}

//  void QSGRenderLoop::releaseResources(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderLoop16releaseResourcesEP12QQuickWindow(
    QSGRenderLoop *self,
    QQuickWindow *window) {
  self->releaseResources(window);
}

//  void QSGRenderLoop::postJob(QQuickWindow *window, QRunnable *job)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderLoop7postJobEP12QQuickWindowP9QRunnable(
    QSGRenderLoop *self,
    QQuickWindow *window,
    QRunnable *job) {
  self->postJob(window, job);
}

//  void QSGRenderLoop::addWindow(QQuickWindow *win)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderLoop9addWindowEP12QQuickWindow(
    QSGRenderLoop *self,
    QQuickWindow *win) {
  self->addWindow(win);
}

//  void QSGRenderLoop::removeWindow(QQuickWindow *win)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderLoop12removeWindowEP12QQuickWindow(
    QSGRenderLoop *self,
    QQuickWindow *win) {
  self->removeWindow(win);
}

//  QSurface::SurfaceType QSGRenderLoop::windowSurfaceType() const
extern "C" Q_DECL_EXPORT
QSurface::SurfaceType ritual_ZNK13QSGRenderLoop17windowSurfaceTypeEv(
    const QSGRenderLoop *self) {
  return self->windowSurfaceType();
}

//  QSGRenderLoop *QSGRenderLoop::instance()
extern "C" Q_DECL_EXPORT
QSGRenderLoop *ritual_ZN13QSGRenderLoop8instanceEv() {
  return QSGRenderLoop::instance();
}

//  void QSGRenderLoop::setInstance(QSGRenderLoop *instance)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderLoop11setInstanceEPS_(QSGRenderLoop *instance) {
  QSGRenderLoop::setInstance(instance);
}

//  bool QSGRenderLoop::interleaveIncubation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QSGRenderLoop20interleaveIncubationEv(
    const QSGRenderLoop *self) {
  return self->interleaveIncubation();
}

//  int QSGRenderLoop::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QSGRenderLoop5flagsEv(const QSGRenderLoop *self) {
  return self->flags();
}

//  void QSGRenderLoop::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderLoop7cleanupEv() {
  QSGRenderLoop::cleanup();
}

//  void QSGRenderLoop::handleContextCreationFailure(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderLoop28handleContextCreationFailureEP12QQuickWindow(
    QSGRenderLoop *self,
    QQuickWindow *window) {
  self->handleContextCreationFailure(window);
}

//  a Python function taken by a CuteQSGRenderLoop, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRenderLoop(
    QSGRenderLoop *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRenderLoop *>(self)->take(key, call);
}

//  void QSGRenderLoop::resize(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QSGRenderLoop6resizeEP12QQuickWindow(
    QSGRenderLoop *self,
    QQuickWindow *a0) {
  self->QSGRenderLoop::resize(a0);
}

//  void QSGRenderLoop::handleUpdateRequest(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QSGRenderLoop19handleUpdateRequestEP12QQuickWindow(
    QSGRenderLoop *self,
    QQuickWindow *a0) {
  self->QSGRenderLoop::handleUpdateRequest(a0);
}

//  void QSGRenderLoop::postJob(QQuickWindow *window, QRunnable *job)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QSGRenderLoop7postJobEP12QQuickWindowP9QRunnable(
    QSGRenderLoop *self,
    QQuickWindow *window,
    QRunnable *job) {
  self->QSGRenderLoop::postJob(window, job);
}

//  QSurface::SurfaceType QSGRenderLoop::windowSurfaceType() const
extern "C" Q_DECL_EXPORT
QSurface::SurfaceType ritual_own_ZNK13QSGRenderLoop17windowSurfaceTypeEv(
    const QSGRenderLoop *self) {
  return self->QSGRenderLoop::windowSurfaceType();
}

//  bool QSGRenderLoop::interleaveIncubation() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QSGRenderLoop20interleaveIncubationEv(
    const QSGRenderLoop *self) {
  return self->QSGRenderLoop::interleaveIncubation();
}

//  int QSGRenderLoop::flags() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QSGRenderLoop5flagsEv(const QSGRenderLoop *self) {
  return self->QSGRenderLoop::flags();
}
