//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3dtexture_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/qt3dquickrender_global_p.h>
#include <Qt3DQuickRender/Qt3DQuickRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3dtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <Qt3DRender/Qt3DRender>

//  A Qt3DRender::Render::Quick::Quick3DTextureExtension that Python can take functions over in. Every Qt3DRender::Render::Quick::Quick3DTextureExtension
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_Render_Quick_Quick3DTextureExtension : public Qt3DRender::Render::Quick::Quick3DTextureExtension {
public:
  using Qt3DRender::Render::Quick::Quick3DTextureExtension::Quick3DTextureExtension;
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
      CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall0 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall0>(taken[0]);
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
      CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall1 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall1>(taken[1]);
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
      CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall2 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall2>(taken[2]);
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
      CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall3 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall3>(taken[3]);
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
      CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall4 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall4>(taken[4]);
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
      CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall5 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall5>(taken[5]);
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
      CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall6 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DTextureExtensionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *Qt3DRender::Render::Quick::Quick3DTextureExtension::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender6Render5Quick23Quick3DTextureExtension10metaObjectEv(
    const Qt3DRender::Render::Quick::Quick3DTextureExtension *self) {
  return self->metaObject();
}

//  void
//      *Qt3DRender::Render::Quick::Quick3DTextureExtension::qt_metacast(cons
//      t char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender6Render5Quick23Quick3DTextureExtension11qt_metacastEPKc(
    Qt3DRender::Render::Quick::Quick3DTextureExtension *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::Render::Quick::Quick3DTextureExtension::qt_metacall(QMeta
//      Object::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender6Render5Quick23Quick3DTextureExtension11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::Render::Quick::Quick3DTextureExtension *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::Render::Quick::Quick3DTextureExtension::tr(const char
//      *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender6Render5Quick23Quick3DTextureExtension2trEPKcS4_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DRender::Render::Quick::Quick3DTextureExtension::tr(
          s,
          c,
          n));
}

//  Qt3DRender::Render::Quick::Quick3DTextureExtension::Quick3DTextureExtensi
//      on(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Quick::Quick3DTextureExtension *ritual_ZN10Qt3DRender6Render5Quick23Quick3DTextureExtensionC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DRender_Render_Quick_Quick3DTextureExtension(parent);
}

//  QQmlListProperty<QAbstractTextureImage>
//      Qt3DRender::Render::Quick::Quick3DTextureExtension::textureImages()
extern "C" Q_DECL_EXPORT
QQmlListProperty<Qt3DRender::QAbstractTextureImage> *ritual_ZN10Qt3DRender6Render5Quick23Quick3DTextureExtension13textureImagesEv(
    Qt3DRender::Render::Quick::Quick3DTextureExtension *self) {
  return new QQmlListProperty<Qt3DRender::QAbstractTextureImage>(
      self->textureImages());
}

//  QAbstractTexture
//      *Qt3DRender::Render::Quick::Quick3DTextureExtension::parentTexture()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture *ritual_ZNK10Qt3DRender6Render5Quick23Quick3DTextureExtension13parentTextureEv(
    const Qt3DRender::Render::Quick::Quick3DTextureExtension *self) {
  return self->parentTexture();
}

//  a Python function taken by a
//      CuteQt3DRender_Render_Quick_Quick3DTextureExtension, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_Quick_Quick3DTextureExtension(
    Qt3DRender::Render::Quick::Quick3DTextureExtension *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_Quick_Quick3DTextureExtension *>(self)->take(key, call);
}

//  a QQmlListProperty<Qt3DRender::QAbstractTextureImage> a ritual of
//      Qt3DRender::Render::Quick::Quick3DTextureExtension gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_Quick_Quick3DTextureExtension__QQmlListProperty_Qt3DRender_QAbstractTextureImage(
    QQmlListProperty<Qt3DRender::QAbstractTextureImage> *self) {
  delete self;
}
