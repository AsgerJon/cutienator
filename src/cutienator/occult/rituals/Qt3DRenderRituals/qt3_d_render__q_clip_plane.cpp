//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qclipplane.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qclipplane.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QClipPlane that Python can take functions over in. Every Qt3DRender::QClipPlane
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QClipPlaneCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QClipPlaneCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QClipPlaneCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QClipPlaneCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QClipPlaneCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QClipPlaneCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QClipPlaneCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QClipPlane : public Qt3DRender::QClipPlane {
public:
  using Qt3DRender::QClipPlane::QClipPlane;
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
      CuteQt3DRender_QClipPlaneCall0 call = reinterpret_cast<CuteQt3DRender_QClipPlaneCall0>(taken[0]);
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
      CuteQt3DRender_QClipPlaneCall1 call = reinterpret_cast<CuteQt3DRender_QClipPlaneCall1>(taken[1]);
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
      CuteQt3DRender_QClipPlaneCall2 call = reinterpret_cast<CuteQt3DRender_QClipPlaneCall2>(taken[2]);
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
      CuteQt3DRender_QClipPlaneCall3 call = reinterpret_cast<CuteQt3DRender_QClipPlaneCall3>(taken[3]);
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
      CuteQt3DRender_QClipPlaneCall4 call = reinterpret_cast<CuteQt3DRender_QClipPlaneCall4>(taken[4]);
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
      CuteQt3DRender_QClipPlaneCall5 call = reinterpret_cast<CuteQt3DRender_QClipPlaneCall5>(taken[5]);
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
      CuteQt3DRender_QClipPlaneCall6 call = reinterpret_cast<CuteQt3DRender_QClipPlaneCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QClipPlane::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender10QClipPlane10metaObjectEv(
    const Qt3DRender::QClipPlane *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QClipPlane::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender10QClipPlane11qt_metacastEPKc(
    Qt3DRender::QClipPlane *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QClipPlane::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender10QClipPlane11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QClipPlane *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QClipPlane::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender10QClipPlane2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QClipPlane::tr(s, c, n));
}

//  Qt3DRender::QClipPlane::QClipPlane(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QClipPlane *ritual_ZN10Qt3DRender10QClipPlaneC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QClipPlane(parent);
}

//  Qt3DRender::QClipPlane::~QClipPlane()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QClipPlaneD1Ev(Qt3DRender::QClipPlane *self) {
  delete self;
}

//  int Qt3DRender::QClipPlane::planeIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender10QClipPlane10planeIndexEv(
    const Qt3DRender::QClipPlane *self) {
  return self->planeIndex();
}

//  QVector3D Qt3DRender::QClipPlane::normal() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender10QClipPlane6normalEv(
    const Qt3DRender::QClipPlane *self) {
  return new QVector3D(self->normal());
}

//  float Qt3DRender::QClipPlane::distance() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender10QClipPlane8distanceEv(
    const Qt3DRender::QClipPlane *self) {
  return self->distance();
}

//  void Qt3DRender::QClipPlane::setPlaneIndex(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QClipPlane13setPlaneIndexEi(
    Qt3DRender::QClipPlane *self,
    int a0) {
  self->setPlaneIndex(a0);
}

//  void Qt3DRender::QClipPlane::setNormal(QVector3D a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QClipPlane9setNormalE9QVector3D(
    Qt3DRender::QClipPlane *self,
    const QVector3D *a0) {
  self->setNormal(*a0);
}

//  void Qt3DRender::QClipPlane::setDistance(float a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QClipPlane11setDistanceEf(
    Qt3DRender::QClipPlane *self,
    float a0) {
  self->setDistance(a0);
}

//  void Qt3DRender::QClipPlane::planeIndexChanged(int planeIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QClipPlane17planeIndexChangedEi(
    Qt3DRender::QClipPlane *self,
    int planeIndex) {
  self->planeIndexChanged(planeIndex);
}

//  void Qt3DRender::QClipPlane::normalChanged(QVector3D normal)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QClipPlane13normalChangedE9QVector3D(
    Qt3DRender::QClipPlane *self,
    const QVector3D *normal) {
  self->normalChanged(*normal);
}

//  void Qt3DRender::QClipPlane::distanceChanged(float distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QClipPlane15distanceChangedEf(
    Qt3DRender::QClipPlane *self,
    float distance) {
  self->distanceChanged(distance);
}

//  QClipPlanePrivate *Qt3DRender::QClipPlane::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QClipPlanePrivate *ritual_ZN10Qt3DRender10QClipPlane6d_funcEv(
    Qt3DRender::QClipPlane *self) {
  return self->d_func();
}

//  const QClipPlanePrivate *Qt3DRender::QClipPlane::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QClipPlanePrivate *ritual_ZNK10Qt3DRender10QClipPlane6d_funcEv(
    const Qt3DRender::QClipPlane *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QClipPlane, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QClipPlane(
    Qt3DRender::QClipPlane *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QClipPlane *>(self)->take(key, call);
}
