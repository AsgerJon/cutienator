//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwltextureorphanage_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwltextureorphanage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QtWayland::QWaylandTextureOrphanage that Python can take functions over in. Every QtWayland::QWaylandTextureOrphanage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWayland_QWaylandTextureOrphanageCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWayland_QWaylandTextureOrphanageCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_QWaylandTextureOrphanageCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_QWaylandTextureOrphanageCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_QWaylandTextureOrphanageCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_QWaylandTextureOrphanageCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_QWaylandTextureOrphanageCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtWayland_QWaylandTextureOrphanage : public QtWayland::QWaylandTextureOrphanage {
public:
  using QtWayland::QWaylandTextureOrphanage::QWaylandTextureOrphanage;
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
      CuteQtWayland_QWaylandTextureOrphanageCall0 call = reinterpret_cast<CuteQtWayland_QWaylandTextureOrphanageCall0>(taken[0]);
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
      CuteQtWayland_QWaylandTextureOrphanageCall1 call = reinterpret_cast<CuteQtWayland_QWaylandTextureOrphanageCall1>(taken[1]);
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
      CuteQtWayland_QWaylandTextureOrphanageCall2 call = reinterpret_cast<CuteQtWayland_QWaylandTextureOrphanageCall2>(taken[2]);
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
      CuteQtWayland_QWaylandTextureOrphanageCall3 call = reinterpret_cast<CuteQtWayland_QWaylandTextureOrphanageCall3>(taken[3]);
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
      CuteQtWayland_QWaylandTextureOrphanageCall4 call = reinterpret_cast<CuteQtWayland_QWaylandTextureOrphanageCall4>(taken[4]);
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
      CuteQtWayland_QWaylandTextureOrphanageCall5 call = reinterpret_cast<CuteQtWayland_QWaylandTextureOrphanageCall5>(taken[5]);
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
      CuteQtWayland_QWaylandTextureOrphanageCall6 call = reinterpret_cast<CuteQtWayland_QWaylandTextureOrphanageCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtWayland::QWaylandTextureOrphanage::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QtWayland24QWaylandTextureOrphanage10metaObjectEv(
    const QtWayland::QWaylandTextureOrphanage *self) {
  return self->metaObject();
}

//  void *QtWayland::QWaylandTextureOrphanage::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QtWayland24QWaylandTextureOrphanage11qt_metacastEPKc(
    QtWayland::QWaylandTextureOrphanage *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtWayland::QWaylandTextureOrphanage::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtWayland24QWaylandTextureOrphanage11qt_metacallEN11QMetaObject4CallEiPPv(
    QtWayland::QWaylandTextureOrphanage *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtWayland::QWaylandTextureOrphanage::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QtWayland24QWaylandTextureOrphanage2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtWayland::QWaylandTextureOrphanage::tr(s, c, n));
}

//  QtWayland::QWaylandTextureOrphanage::QWaylandTextureOrphanage()
extern "C" Q_DECL_EXPORT
QtWayland::QWaylandTextureOrphanage *ritual_ZN9QtWayland24QWaylandTextureOrphanageC1Ev() {
  return new CuteQtWayland_QWaylandTextureOrphanage();
}

//  QtWayland::QWaylandTextureOrphanage::~QWaylandTextureOrphanage()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland24QWaylandTextureOrphanageD1Ev(
    QtWayland::QWaylandTextureOrphanage *self) {
  delete self;
}

//  QWaylandTextureOrphanage *QtWayland::QWaylandTextureOrphanage::instance()
extern "C" Q_DECL_EXPORT
QtWayland::QWaylandTextureOrphanage *ritual_ZN9QtWayland24QWaylandTextureOrphanage8instanceEv() {
  return QtWayland::QWaylandTextureOrphanage::instance();
}

//  void QtWayland::QWaylandTextureOrphanage::admitTexture(QOpenGLTexture
//      *tex, QOpenGLContext *ctx)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland24QWaylandTextureOrphanage12admitTextureEP14QOpenGLTextureP14QOpenGLContext(
    QtWayland::QWaylandTextureOrphanage *self,
    QOpenGLTexture *tex,
    QOpenGLContext *ctx) {
  self->admitTexture(tex, ctx);
}

//  void QtWayland::QWaylandTextureOrphanage::deleteTextures()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland24QWaylandTextureOrphanage14deleteTexturesEv(
    QtWayland::QWaylandTextureOrphanage *self) {
  self->deleteTextures();
}

//  void QtWayland::QWaylandTextureOrphanage::onContextAboutToBeDestroyed(QOp
//      enGLContext *ctx)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland24QWaylandTextureOrphanage27onContextAboutToBeDestroyedEP14QOpenGLContext(
    QtWayland::QWaylandTextureOrphanage *self,
    QOpenGLContext *ctx) {
  self->onContextAboutToBeDestroyed(ctx);
}

//  void QtWayland::QWaylandTextureOrphanage::deleteTexturesByContext(QOpenGL
//      Context *ctx)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland24QWaylandTextureOrphanage23deleteTexturesByContextEP14QOpenGLContext(
    QtWayland::QWaylandTextureOrphanage *self,
    QOpenGLContext *ctx) {
  self->deleteTexturesByContext(ctx);
}

//  a Python function taken by a CuteQtWayland_QWaylandTextureOrphanage, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtWayland_QWaylandTextureOrphanage(
    QtWayland::QWaylandTextureOrphanage *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtWayland_QWaylandTextureOrphanage *>(self)->take(key, call);
}

#endif  // QT_CONFIG(opengl)
