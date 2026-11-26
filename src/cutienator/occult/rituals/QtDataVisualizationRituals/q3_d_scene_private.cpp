//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/q3dscene_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/q3dscene_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Q3DScenePrivate that Python can take functions over in. Every Q3DScenePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DScenePrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DScenePrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScenePrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScenePrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScenePrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScenePrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScenePrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DScenePrivate : public Q3DScenePrivate {
public:
  using Q3DScenePrivate::Q3DScenePrivate;
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
      CuteQ3DScenePrivateCall0 call = reinterpret_cast<CuteQ3DScenePrivateCall0>(taken[0]);
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
      CuteQ3DScenePrivateCall1 call = reinterpret_cast<CuteQ3DScenePrivateCall1>(taken[1]);
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
      CuteQ3DScenePrivateCall2 call = reinterpret_cast<CuteQ3DScenePrivateCall2>(taken[2]);
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
      CuteQ3DScenePrivateCall3 call = reinterpret_cast<CuteQ3DScenePrivateCall3>(taken[3]);
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
      CuteQ3DScenePrivateCall4 call = reinterpret_cast<CuteQ3DScenePrivateCall4>(taken[4]);
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
      CuteQ3DScenePrivateCall5 call = reinterpret_cast<CuteQ3DScenePrivateCall5>(taken[5]);
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
      CuteQ3DScenePrivateCall6 call = reinterpret_cast<CuteQ3DScenePrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DScenePrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15Q3DScenePrivate10metaObjectEv(
    const Q3DScenePrivate *self) {
  return self->metaObject();
}

//  void *Q3DScenePrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15Q3DScenePrivate11qt_metacastEPKc(
    Q3DScenePrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Q3DScenePrivate::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15Q3DScenePrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    Q3DScenePrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Q3DScenePrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15Q3DScenePrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Q3DScenePrivate::tr(s, c, n));
}

//  Q3DScenePrivate::Q3DScenePrivate(Q3DScene *q)
extern "C" Q_DECL_EXPORT
Q3DScenePrivate *ritual_ZN15Q3DScenePrivateC1EP8Q3DScene(Q3DScene *q) {
  return new CuteQ3DScenePrivate(q);
}

//  Q3DScenePrivate::~Q3DScenePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivateD1Ev(Q3DScenePrivate *self) {
  delete self;
}

//  void Q3DScenePrivate::sync(Q3DScenePrivate &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivate4syncERS_(
    Q3DScenePrivate *self,
    Q3DScenePrivate *other) {
  self->sync(*other);
}

//  void Q3DScenePrivate::setViewport(const QRect &viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivate11setViewportERK5QRect(
    Q3DScenePrivate *self,
    const QRect *viewport) {
  self->setViewport(*viewport);
}

//  void Q3DScenePrivate::setViewportSize(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivate15setViewportSizeEii(
    Q3DScenePrivate *self,
    int width,
    int height) {
  self->setViewportSize(width, height);
}

//  void Q3DScenePrivate::setWindowSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivate13setWindowSizeERK5QSize(
    Q3DScenePrivate *self,
    const QSize *size) {
  self->setWindowSize(*size);
}

//  QSize Q3DScenePrivate::windowSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15Q3DScenePrivate10windowSizeEv(
    const Q3DScenePrivate *self) {
  return new QSize(self->windowSize());
}

//  void Q3DScenePrivate::calculateSubViewports()
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivate21calculateSubViewportsEv(
    Q3DScenePrivate *self) {
  self->calculateSubViewports();
}

//  void Q3DScenePrivate::updateGLViewport()
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivate16updateGLViewportEv(Q3DScenePrivate *self) {
  self->updateGLViewport();
}

//  void Q3DScenePrivate::updateGLSubViewports()
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivate20updateGLSubViewportsEv(
    Q3DScenePrivate *self) {
  self->updateGLSubViewports();
}

//  QRect Q3DScenePrivate::glViewport()
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN15Q3DScenePrivate10glViewportEv(Q3DScenePrivate *self) {
  return new QRect(self->glViewport());
}

//  QRect Q3DScenePrivate::glPrimarySubViewport()
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN15Q3DScenePrivate20glPrimarySubViewportEv(
    Q3DScenePrivate *self) {
  return new QRect(self->glPrimarySubViewport());
}

//  QRect Q3DScenePrivate::glSecondarySubViewport()
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN15Q3DScenePrivate22glSecondarySubViewportEv(
    Q3DScenePrivate *self) {
  return new QRect(self->glSecondarySubViewport());
}

//  void Q3DScenePrivate::setLightPositionRelativeToCamera(const QVector3D
//      &relativePosition, float fixedRotation, float distanceModifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivate32setLightPositionRelativeToCameraERK9QVector3Dff(
    Q3DScenePrivate *self,
    const QVector3D *relativePosition,
    float fixedRotation,
    float distanceModifier) {
  self->setLightPositionRelativeToCamera(
      *relativePosition,
      fixedRotation,
      distanceModifier);
}

//  void Q3DScenePrivate::markDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivate9markDirtyEv(Q3DScenePrivate *self) {
  self->markDirty();
}

//  bool Q3DScenePrivate::isInArea(const QRect &area, int x, int y) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15Q3DScenePrivate8isInAreaERK5QRectii(
    const Q3DScenePrivate *self,
    const QRect *area,
    int x,
    int y) {
  return self->isInArea(*area, x, y);
}

//  void Q3DScenePrivate::needRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DScenePrivate10needRenderEv(Q3DScenePrivate *self) {
  self->needRender();
}

//  a Python function taken by a CuteQ3DScenePrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DScenePrivate(
    Q3DScenePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQ3DScenePrivate *>(self)->take(key, call);
}
