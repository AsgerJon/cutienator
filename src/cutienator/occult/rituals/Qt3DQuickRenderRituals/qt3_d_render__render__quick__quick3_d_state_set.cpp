//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3dstateset_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/qt3dquickrender_global_p.h>
#include <Qt3DQuickRender/Qt3DQuickRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3dstateset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <Qt3DRender/Qt3DRender>

//  A Qt3DRender::Render::Quick::Quick3DStateSet that Python can take functions over in. Every Qt3DRender::Render::Quick::Quick3DStateSet
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Render_Quick_Quick3DStateSetCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Render_Quick_Quick3DStateSetCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_Quick3DStateSetCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_Quick3DStateSetCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_Quick3DStateSetCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_Quick3DStateSetCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_Quick3DStateSetCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_Render_Quick_Quick3DStateSet : public Qt3DRender::Render::Quick::Quick3DStateSet {
public:
  using Qt3DRender::Render::Quick::Quick3DStateSet::Quick3DStateSet;
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
      CuteQt3DRender_Render_Quick_Quick3DStateSetCall0 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DStateSetCall0>(taken[0]);
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
      CuteQt3DRender_Render_Quick_Quick3DStateSetCall1 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DStateSetCall1>(taken[1]);
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
      CuteQt3DRender_Render_Quick_Quick3DStateSetCall2 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DStateSetCall2>(taken[2]);
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
      CuteQt3DRender_Render_Quick_Quick3DStateSetCall3 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DStateSetCall3>(taken[3]);
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
      CuteQt3DRender_Render_Quick_Quick3DStateSetCall4 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DStateSetCall4>(taken[4]);
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
      CuteQt3DRender_Render_Quick_Quick3DStateSetCall5 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DStateSetCall5>(taken[5]);
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
      CuteQt3DRender_Render_Quick_Quick3DStateSetCall6 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DStateSetCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *Qt3DRender::Render::Quick::Quick3DStateSet::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender6Render5Quick15Quick3DStateSet10metaObjectEv(
    const Qt3DRender::Render::Quick::Quick3DStateSet *self) {
  return self->metaObject();
}

//  void *Qt3DRender::Render::Quick::Quick3DStateSet::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender6Render5Quick15Quick3DStateSet11qt_metacastEPKc(
    Qt3DRender::Render::Quick::Quick3DStateSet *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int
//      Qt3DRender::Render::Quick::Quick3DStateSet::qt_metacall(QMetaObject::
//      Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender6Render5Quick15Quick3DStateSet11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::Render::Quick::Quick3DStateSet *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::Render::Quick::Quick3DStateSet::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender6Render5Quick15Quick3DStateSet2trEPKcS4_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DRender::Render::Quick::Quick3DStateSet::tr(
          s,
          c,
          n));
}

//  Qt3DRender::Render::Quick::Quick3DStateSet::Quick3DStateSet(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Quick::Quick3DStateSet *ritual_ZN10Qt3DRender6Render5Quick15Quick3DStateSetC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DRender_Render_Quick_Quick3DStateSet(parent);
}

//  Qt3DRender::Render::Quick::Quick3DStateSet::~Quick3DStateSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Quick15Quick3DStateSetD1Ev(
    Qt3DRender::Render::Quick::Quick3DStateSet *self) {
  delete self;
}

//  QQmlListProperty<QRenderState>
//      Qt3DRender::Render::Quick::Quick3DStateSet::renderStateList()
extern "C" Q_DECL_EXPORT
QQmlListProperty<Qt3DRender::QRenderState> *ritual_ZN10Qt3DRender6Render5Quick15Quick3DStateSet15renderStateListEv(
    Qt3DRender::Render::Quick::Quick3DStateSet *self) {
  return new QQmlListProperty<Qt3DRender::QRenderState>(
      self->renderStateList());
}

//  QRenderStateSet
//      *Qt3DRender::Render::Quick::Quick3DStateSet::parentStateSet() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderStateSet *ritual_ZNK10Qt3DRender6Render5Quick15Quick3DStateSet14parentStateSetEv(
    const Qt3DRender::Render::Quick::Quick3DStateSet *self) {
  return self->parentStateSet();
}

//  a Python function taken by a CuteQt3DRender_Render_Quick_Quick3DStateSet,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_Quick_Quick3DStateSet(
    Qt3DRender::Render::Quick::Quick3DStateSet *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_Quick_Quick3DStateSet *>(self)->take(key, call);
}

//  a QQmlListProperty<Qt3DRender::QRenderState> a ritual of
//      Qt3DRender::Render::Quick::Quick3DStateSet gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_Quick_Quick3DStateSet__QQmlListProperty_Qt3DRender_QRenderState(
    QQmlListProperty<Qt3DRender::QRenderState> *self) {
  delete self;
}
