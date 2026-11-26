//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickTransform that Python can take functions over in. Every QQuickTransform
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickTransformCall0)(const void *, QMatrix4x4 *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTransformCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTransformCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTransformCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTransformCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTransformCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTransformCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTransformCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTransform : public QQuickTransform {
public:
  using QQuickTransform::QQuickTransform;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QQuickTransform7applyToEP10QMatrix4x4")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickTransform::applyTo(QMatrix4x4 *matrix) const
  void applyTo(QMatrix4x4 *matrix) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTransformCall0 call = reinterpret_cast<CuteQQuickTransformCall0>(taken[0]);
      call(this, matrix, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTransformCall1 call = reinterpret_cast<CuteQQuickTransformCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTransformCall2 call = reinterpret_cast<CuteQQuickTransformCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTransformCall3 call = reinterpret_cast<CuteQQuickTransformCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTransformCall4 call = reinterpret_cast<CuteQQuickTransformCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTransformCall5 call = reinterpret_cast<CuteQQuickTransformCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTransformCall6 call = reinterpret_cast<CuteQQuickTransformCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTransformCall7 call = reinterpret_cast<CuteQQuickTransformCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTransform::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickTransform10metaObjectEv(
    const QQuickTransform *self) {
  return self->metaObject();
}

//  void *QQuickTransform::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQuickTransform11qt_metacastEPKc(
    QQuickTransform *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTransform::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQuickTransform11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTransform *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTransform::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickTransform2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTransform::tr(s, c, n));
}

//  void QQuickTransform::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTransform22qt_qmlMarker_anonymousEv(
    QQuickTransform *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickTransform::QQuickTransform(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickTransform *ritual_ZN15QQuickTransformC1EP7QObject(QObject *parent) {
  return new CuteQQuickTransform(parent);
}

//  QQuickTransform::~QQuickTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTransformD1Ev(QQuickTransform *self) {
  delete self;
}

//  void QQuickTransform::appendToItem(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTransform12appendToItemEP10QQuickItem(
    QQuickTransform *self,
    QQuickItem *a0) {
  self->appendToItem(a0);
}

//  void QQuickTransform::prependToItem(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTransform13prependToItemEP10QQuickItem(
    QQuickTransform *self,
    QQuickItem *a0) {
  self->prependToItem(a0);
}

//  void QQuickTransform::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QQuickTransform7applyToEP10QMatrix4x4(
    const QQuickTransform *self,
    QMatrix4x4 *matrix) {
  self->applyTo(matrix);
}

//  void QQuickTransform::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTransform6updateEv(QQuickTransform *self) {
  self->update();
}

//  QQuickTransform::QQuickTransform(QQuickTransformPrivate &dd, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickTransform *ritual_ZN15QQuickTransformC1ER22QQuickTransformPrivateP7QObject(
    QQuickTransformPrivate *dd,
    QObject *parent) {
  return new CuteQQuickTransform(*dd, parent);
}

//  QQuickTransformPrivate *QQuickTransform::d_func()
extern "C" Q_DECL_EXPORT
QQuickTransformPrivate *ritual_ZN15QQuickTransform6d_funcEv(
    QQuickTransform *self) {
  return self->d_func();
}

//  const QQuickTransformPrivate *QQuickTransform::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickTransformPrivate *ritual_ZNK15QQuickTransform6d_funcEv(
    const QQuickTransform *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickTransform, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTransform(
    QQuickTransform *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTransform *>(self)->take(key, call);
}
