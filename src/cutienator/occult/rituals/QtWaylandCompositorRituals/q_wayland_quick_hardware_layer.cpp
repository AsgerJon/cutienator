//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandquickhardwarelayer_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(opengl) && QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandquickhardwarelayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWaylandQuickHardwareLayer that Python can take functions over in. Every QWaylandQuickHardwareLayer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandQuickHardwareLayerCall0)(const void *, int *);
typedef void (*CuteQWaylandQuickHardwareLayerCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandQuickHardwareLayerCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandQuickHardwareLayerCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickHardwareLayerCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickHardwareLayerCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickHardwareLayerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickHardwareLayerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickHardwareLayerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandQuickHardwareLayer : public QWaylandQuickHardwareLayer {
public:
  using QWaylandQuickHardwareLayer::QWaylandQuickHardwareLayer;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QWaylandQuickHardwareLayer::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandQuickHardwareLayerCall0 call = reinterpret_cast<CuteQWaylandQuickHardwareLayerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandQuickHardwareLayer::classBegin();
  }

  //  void QWaylandQuickHardwareLayer::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandQuickHardwareLayerCall1 call = reinterpret_cast<CuteQWaylandQuickHardwareLayerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandQuickHardwareLayer::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandQuickHardwareLayerCall2 call = reinterpret_cast<CuteQWaylandQuickHardwareLayerCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWaylandQuickHardwareLayerCall3 call = reinterpret_cast<CuteQWaylandQuickHardwareLayerCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWaylandQuickHardwareLayerCall4 call = reinterpret_cast<CuteQWaylandQuickHardwareLayerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWaylandQuickHardwareLayerCall5 call = reinterpret_cast<CuteQWaylandQuickHardwareLayerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWaylandQuickHardwareLayerCall6 call = reinterpret_cast<CuteQWaylandQuickHardwareLayerCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWaylandQuickHardwareLayerCall7 call = reinterpret_cast<CuteQWaylandQuickHardwareLayerCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWaylandQuickHardwareLayerCall8 call = reinterpret_cast<CuteQWaylandQuickHardwareLayerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandQuickHardwareLayer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QWaylandQuickHardwareLayer10metaObjectEv(
    const QWaylandQuickHardwareLayer *self) {
  return self->metaObject();
}

//  QString QWaylandQuickHardwareLayer::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QWaylandQuickHardwareLayer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandQuickHardwareLayer::tr(s, c, n));
}

//  QWaylandQuickHardwareLayer::QWaylandQuickHardwareLayer(QObject *parent)
extern "C" Q_DECL_EXPORT
QWaylandQuickHardwareLayer *ritual_ZN26QWaylandQuickHardwareLayerC1EP7QObject(
    QObject *parent) {
  return new CuteQWaylandQuickHardwareLayer(parent);
}

//  QWaylandQuickHardwareLayer::~QWaylandQuickHardwareLayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWaylandQuickHardwareLayerD1Ev(
    QWaylandQuickHardwareLayer *self) {
  delete self;
}

//  int QWaylandQuickHardwareLayer::stackingLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QWaylandQuickHardwareLayer13stackingLevelEv(
    const QWaylandQuickHardwareLayer *self) {
  return self->stackingLevel();
}

//  void QWaylandQuickHardwareLayer::setStackingLevel(int level)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWaylandQuickHardwareLayer16setStackingLevelEi(
    QWaylandQuickHardwareLayer *self,
    int level) {
  self->setStackingLevel(level);
}

//  QWaylandQuickItem *QWaylandQuickHardwareLayer::waylandItem() const
extern "C" Q_DECL_EXPORT
QWaylandQuickItem *ritual_ZNK26QWaylandQuickHardwareLayer11waylandItemEv(
    const QWaylandQuickHardwareLayer *self) {
  return self->waylandItem();
}

//  void QWaylandQuickHardwareLayer::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWaylandQuickHardwareLayer10classBeginEv(
    QWaylandQuickHardwareLayer *self) {
  self->classBegin();
}

//  void QWaylandQuickHardwareLayer::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWaylandQuickHardwareLayer17componentCompleteEv(
    QWaylandQuickHardwareLayer *self) {
  self->componentComplete();
}

//  void QWaylandQuickHardwareLayer::setSceneGraphPainting(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWaylandQuickHardwareLayer21setSceneGraphPaintingEb(
    QWaylandQuickHardwareLayer *self,
    bool a0) {
  self->setSceneGraphPainting(a0);
}

//  void QWaylandQuickHardwareLayer::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWaylandQuickHardwareLayer10initializeEv(
    QWaylandQuickHardwareLayer *self) {
  self->initialize();
}

//  QWaylandQuickHardwareLayer as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QWaylandQuickHardwareLayer_QQmlParserStatus(
    QWaylandQuickHardwareLayer *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQWaylandQuickHardwareLayer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandQuickHardwareLayer(
    QWaylandQuickHardwareLayer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandQuickHardwareLayer *>(self)->take(key, call);
}

//  void QWaylandQuickHardwareLayer::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QWaylandQuickHardwareLayer10classBeginEv(
    QWaylandQuickHardwareLayer *self) {
  self->QWaylandQuickHardwareLayer::classBegin();
}

//  void QWaylandQuickHardwareLayer::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QWaylandQuickHardwareLayer17componentCompleteEv(
    QWaylandQuickHardwareLayer *self) {
  self->QWaylandQuickHardwareLayer::componentComplete();
}

#endif  // QT_CONFIG(opengl) && QT_CONFIG(wayland_compositor_quick)
