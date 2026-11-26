//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickrectangle_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickrectangle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtGui/QGradientStops>

//  A QQuickGradient that Python can take functions over in. Every QQuickGradient
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGradientCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGradientCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGradientCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGradientCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGradientCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGradientCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGradientCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickGradient : public QQuickGradient {
public:
  using QQuickGradient::QQuickGradient;
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
      CuteQQuickGradientCall0 call = reinterpret_cast<CuteQQuickGradientCall0>(taken[0]);
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
      CuteQQuickGradientCall1 call = reinterpret_cast<CuteQQuickGradientCall1>(taken[1]);
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
      CuteQQuickGradientCall2 call = reinterpret_cast<CuteQQuickGradientCall2>(taken[2]);
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
      CuteQQuickGradientCall3 call = reinterpret_cast<CuteQQuickGradientCall3>(taken[3]);
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
      CuteQQuickGradientCall4 call = reinterpret_cast<CuteQQuickGradientCall4>(taken[4]);
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
      CuteQQuickGradientCall5 call = reinterpret_cast<CuteQQuickGradientCall5>(taken[5]);
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
      CuteQQuickGradientCall6 call = reinterpret_cast<CuteQQuickGradientCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickGradient::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickGradient10metaObjectEv(
    const QQuickGradient *self) {
  return self->metaObject();
}

//  void *QQuickGradient::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickGradient11qt_metacastEPKc(
    QQuickGradient *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickGradient::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickGradient11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickGradient *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickGradient::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickGradient2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGradient::tr(s, c, n));
}

//  const QMetaObject *QQuickGradient::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN14QQuickGradient20qmlExtendedNamespaceEv() {
  return QQuickGradient::qmlExtendedNamespace();
}

//  void QQuickGradient::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGradient30qt_qmlMarker_extendedNamespaceEv(
    QQuickGradient *self) {
  self->qt_qmlMarker_extendedNamespace();
}

//  QQuickGradient::QQuickGradient(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickGradient *ritual_ZN14QQuickGradientC1EP7QObject(QObject *parent) {
  return new CuteQQuickGradient(parent);
}

//  QQuickGradient::~QQuickGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGradientD1Ev(QQuickGradient *self) {
  delete self;
}

//  QQmlListProperty<QQuickGradientStop> QQuickGradient::stops()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuickGradientStop> *ritual_ZN14QQuickGradient5stopsEv(
    QQuickGradient *self) {
  return new QQmlListProperty<QQuickGradientStop>(self->stops());
}

//  Orientation QQuickGradient::orientation() const
extern "C" Q_DECL_EXPORT
QQuickGradient::Orientation ritual_ZNK14QQuickGradient11orientationEv(
    const QQuickGradient *self) {
  return self->orientation();
}

//  void QQuickGradient::setOrientation(Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGradient14setOrientationENS_11OrientationE(
    QQuickGradient *self,
    QQuickGradient::Orientation orientation) {
  self->setOrientation(orientation);
}

//  QGradientStops QQuickGradient::gradientStops() const
extern "C" Q_DECL_EXPORT
QGradientStops *ritual_ZNK14QQuickGradient13gradientStopsEv(
    const QQuickGradient *self) {
  return new QGradientStops(self->gradientStops());
}

//  void QQuickGradient::updated()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGradient7updatedEv(QQuickGradient *self) {
  self->updated();
}

//  void QQuickGradient::orientationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGradient18orientationChangedEv(QQuickGradient *self) {
  self->orientationChanged();
}

//  void QQuickGradient::doUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGradient8doUpdateEv(QQuickGradient *self) {
  self->doUpdate();
}

//  a Python function taken by a CuteQQuickGradient, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickGradient(
    QQuickGradient *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickGradient *>(self)->take(key, call);
}

//  QList<QQuickGradient *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuickGradient *> *ritual_list_make_QQuickGradient_ptr() {
  return new QList<QQuickGradient *>();
}

//  void QList<QQuickGradient *>::append(const QQuickGradient * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuickGradient_ptr(
    QList<QQuickGradient *> *self,
    QQuickGradient *element) {
  self->append(element);
}

//  qsizetype QList<QQuickGradient *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuickGradient_ptr(
    const QList<QQuickGradient *> *self) {
  return self->size();
}

//  const QQuickGradient * &QList<QQuickGradient *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQuickGradient *ritual_list_at_QQuickGradient_ptr(
    const QList<QQuickGradient *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQuickGradient *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuickGradient_ptr(QList<QQuickGradient *> *self) {
  delete self;
}

//  a QQmlListProperty<QQuickGradientStop> a ritual of QQuickGradient gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickGradient__QQmlListProperty_QQuickGradientStop(
    QQmlListProperty<QQuickGradientStop> *self) {
  delete self;
}

//  a QGradientStops a ritual of QQuickGradient gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickGradient__QGradientStops(QGradientStops *self) {
  delete self;
}
