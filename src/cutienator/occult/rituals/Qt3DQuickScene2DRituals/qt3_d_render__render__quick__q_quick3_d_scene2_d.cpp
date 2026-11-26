//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/qt3dquick3dscene2d_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/qt3dquickscene2d_global_p.h>
#include <Qt3DQuickScene2D/Qt3DQuickScene2D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/qt3dquick3dscene2d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <Qt3DCore/Qt3DCore>

//  A Qt3DRender::Render::Quick::QQuick3DScene2D that Python can take functions over in. Every Qt3DRender::Render::Quick::QQuick3DScene2D
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Render_Quick_QQuick3DScene2DCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Render_Quick_QQuick3DScene2DCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_QQuick3DScene2DCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_QQuick3DScene2DCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_QQuick3DScene2DCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_QQuick3DScene2DCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_QQuick3DScene2DCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_Render_Quick_QQuick3DScene2D : public Qt3DRender::Render::Quick::QQuick3DScene2D {
public:
  using Qt3DRender::Render::Quick::QQuick3DScene2D::QQuick3DScene2D;
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
      CuteQt3DRender_Render_Quick_QQuick3DScene2DCall0 call = reinterpret_cast<CuteQt3DRender_Render_Quick_QQuick3DScene2DCall0>(taken[0]);
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
      CuteQt3DRender_Render_Quick_QQuick3DScene2DCall1 call = reinterpret_cast<CuteQt3DRender_Render_Quick_QQuick3DScene2DCall1>(taken[1]);
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
      CuteQt3DRender_Render_Quick_QQuick3DScene2DCall2 call = reinterpret_cast<CuteQt3DRender_Render_Quick_QQuick3DScene2DCall2>(taken[2]);
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
      CuteQt3DRender_Render_Quick_QQuick3DScene2DCall3 call = reinterpret_cast<CuteQt3DRender_Render_Quick_QQuick3DScene2DCall3>(taken[3]);
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
      CuteQt3DRender_Render_Quick_QQuick3DScene2DCall4 call = reinterpret_cast<CuteQt3DRender_Render_Quick_QQuick3DScene2DCall4>(taken[4]);
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
      CuteQt3DRender_Render_Quick_QQuick3DScene2DCall5 call = reinterpret_cast<CuteQt3DRender_Render_Quick_QQuick3DScene2DCall5>(taken[5]);
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
      CuteQt3DRender_Render_Quick_QQuick3DScene2DCall6 call = reinterpret_cast<CuteQt3DRender_Render_Quick_QQuick3DScene2DCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *Qt3DRender::Render::Quick::QQuick3DScene2D::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender6Render5Quick15QQuick3DScene2D10metaObjectEv(
    const Qt3DRender::Render::Quick::QQuick3DScene2D *self) {
  return self->metaObject();
}

//  void *Qt3DRender::Render::Quick::QQuick3DScene2D::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender6Render5Quick15QQuick3DScene2D11qt_metacastEPKc(
    Qt3DRender::Render::Quick::QQuick3DScene2D *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int
//      Qt3DRender::Render::Quick::QQuick3DScene2D::qt_metacall(QMetaObject::
//      Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender6Render5Quick15QQuick3DScene2D11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::Render::Quick::QQuick3DScene2D *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::Render::Quick::QQuick3DScene2D::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender6Render5Quick15QQuick3DScene2D2trEPKcS4_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DRender::Render::Quick::QQuick3DScene2D::tr(
          s,
          c,
          n));
}

//  Qt3DRender::Render::Quick::QQuick3DScene2D::QQuick3DScene2D(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Quick::QQuick3DScene2D *ritual_ZN10Qt3DRender6Render5Quick15QQuick3DScene2DC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DRender_Render_Quick_QQuick3DScene2D(parent);
}

//  Qt3DRender::Quick::QScene2D
//      *Qt3DRender::Render::Quick::QQuick3DScene2D::parentScene2D() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Quick::QScene2D *ritual_ZNK10Qt3DRender6Render5Quick15QQuick3DScene2D13parentScene2DEv(
    const Qt3DRender::Render::Quick::QQuick3DScene2D *self) {
  return self->parentScene2D();
}

//  QQmlListProperty<Qt3DCore::QEntity>
//      Qt3DRender::Render::Quick::QQuick3DScene2D::entities()
extern "C" Q_DECL_EXPORT
QQmlListProperty<Qt3DCore::QEntity> *ritual_ZN10Qt3DRender6Render5Quick15QQuick3DScene2D8entitiesEv(
    Qt3DRender::Render::Quick::QQuick3DScene2D *self) {
  return new QQmlListProperty<Qt3DCore::QEntity>(self->entities());
}

//  a Python function taken by a CuteQt3DRender_Render_Quick_QQuick3DScene2D,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_Quick_QQuick3DScene2D(
    Qt3DRender::Render::Quick::QQuick3DScene2D *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_Quick_QQuick3DScene2D *>(self)->take(key, call);
}

//  a QQmlListProperty<Qt3DCore::QEntity> a ritual of
//      Qt3DRender::Render::Quick::QQuick3DScene2D gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_Quick_QQuick3DScene2D__QQmlListProperty_Qt3DCore_QEntity(
    QQmlListProperty<Qt3DCore::QEntity> *self) {
  delete self;
}
