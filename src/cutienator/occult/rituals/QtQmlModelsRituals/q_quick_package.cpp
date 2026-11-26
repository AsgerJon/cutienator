//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qquickpackage_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qquickpackage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  A QQuickPackage that Python can take functions over in. Every QQuickPackage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPackageCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPackageCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPackageCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPackageCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPackageCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPackageCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPackageCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPackage : public QQuickPackage {
public:
  using QQuickPackage::QQuickPackage;
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
      CuteQQuickPackageCall0 call = reinterpret_cast<CuteQQuickPackageCall0>(taken[0]);
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
      CuteQQuickPackageCall1 call = reinterpret_cast<CuteQQuickPackageCall1>(taken[1]);
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
      CuteQQuickPackageCall2 call = reinterpret_cast<CuteQQuickPackageCall2>(taken[2]);
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
      CuteQQuickPackageCall3 call = reinterpret_cast<CuteQQuickPackageCall3>(taken[3]);
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
      CuteQQuickPackageCall4 call = reinterpret_cast<CuteQQuickPackageCall4>(taken[4]);
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
      CuteQQuickPackageCall5 call = reinterpret_cast<CuteQQuickPackageCall5>(taken[5]);
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
      CuteQQuickPackageCall6 call = reinterpret_cast<CuteQQuickPackageCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPackage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQuickPackage10metaObjectEv(
    const QQuickPackage *self) {
  return self->metaObject();
}

//  void *QQuickPackage::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QQuickPackage11qt_metacastEPKc(
    QQuickPackage *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPackage::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QQuickPackage11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPackage *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPackage::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuickPackage2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPackage::tr(s, c, n));
}

//  QQuickPackagePrivate *QQuickPackage::d_func()
extern "C" Q_DECL_EXPORT
QQuickPackagePrivate *ritual_ZN13QQuickPackage6d_funcEv(
    QQuickPackage *self) {
  return self->d_func();
}

//  const QQuickPackagePrivate *QQuickPackage::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickPackagePrivate *ritual_ZNK13QQuickPackage6d_funcEv(
    const QQuickPackage *self) {
  return self->d_func();
}

//  void QQuickPackage::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPackage21qt_qmlMarker_attachedEv(QQuickPackage *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickPackage::QQuickPackage(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPackage *ritual_ZN13QQuickPackageC1EP7QObject(QObject *parent) {
  return new CuteQQuickPackage(parent);
}

//  QQmlListProperty<QObject> QQuickPackage::data()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN13QQuickPackage4dataEv(
    QQuickPackage *self) {
  return new QQmlListProperty<QObject>(self->data());
}

//  QObject *QQuickPackage::part(const QString &a0)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN13QQuickPackage4partERK7QString(
    QQuickPackage *self,
    const QString *a0) {
  return self->part(*a0);
}

//  bool QQuickPackage::hasPart(const QString &a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QQuickPackage7hasPartERK7QString(
    QQuickPackage *self,
    const QString *a0) {
  return self->hasPart(*a0);
}

//  QQuickPackageAttached *QQuickPackage::qmlAttachedProperties(QObject *a0)
extern "C" Q_DECL_EXPORT
QQuickPackageAttached *ritual_ZN13QQuickPackage21qmlAttachedPropertiesEP7QObject(
    QObject *a0) {
  return QQuickPackage::qmlAttachedProperties(a0);
}

//  a Python function taken by a CuteQQuickPackage, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPackage(
    QQuickPackage *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPackage *>(self)->take(key, call);
}

//  a QQmlListProperty<QObject> a ritual of QQuickPackage gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickPackage__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
