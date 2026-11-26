//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dentityloader_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquick_global_p.h>
#include <Qt3DQuick/Qt3DQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dentityloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DCore::Quick::Quick3DEntityLoader that Python can take functions over in. Every Qt3DCore::Quick::Quick3DEntityLoader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_Quick_Quick3DEntityLoaderCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_Quick_Quick3DEntityLoaderCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_Quick3DEntityLoaderCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_Quick3DEntityLoaderCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_Quick3DEntityLoaderCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_Quick3DEntityLoaderCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_Quick3DEntityLoaderCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_Quick_Quick3DEntityLoader : public Qt3DCore::Quick::Quick3DEntityLoader {
public:
  using Qt3DCore::Quick::Quick3DEntityLoader::Quick3DEntityLoader;
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
      CuteQt3DCore_Quick_Quick3DEntityLoaderCall0 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DEntityLoaderCall0>(taken[0]);
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
      CuteQt3DCore_Quick_Quick3DEntityLoaderCall1 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DEntityLoaderCall1>(taken[1]);
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
      CuteQt3DCore_Quick_Quick3DEntityLoaderCall2 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DEntityLoaderCall2>(taken[2]);
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
      CuteQt3DCore_Quick_Quick3DEntityLoaderCall3 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DEntityLoaderCall3>(taken[3]);
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
      CuteQt3DCore_Quick_Quick3DEntityLoaderCall4 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DEntityLoaderCall4>(taken[4]);
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
      CuteQt3DCore_Quick_Quick3DEntityLoaderCall5 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DEntityLoaderCall5>(taken[5]);
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
      CuteQt3DCore_Quick_Quick3DEntityLoaderCall6 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DEntityLoaderCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::Quick::Quick3DEntityLoader::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore5Quick19Quick3DEntityLoader10metaObjectEv(
    const Qt3DCore::Quick::Quick3DEntityLoader *self) {
  return self->metaObject();
}

//  void *Qt3DCore::Quick::Quick3DEntityLoader::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader11qt_metacastEPKc(
    Qt3DCore::Quick::Quick3DEntityLoader *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::Quick::Quick3DEntityLoader::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::Quick::Quick3DEntityLoader *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::Quick::Quick3DEntityLoader::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::Quick::Quick3DEntityLoader::tr(s, c, n));
}

//  Qt3DCore::Quick::Quick3DEntityLoader::Quick3DEntityLoader(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::Quick3DEntityLoader *ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoaderC1EPNS_5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_Quick_Quick3DEntityLoader(parent);
}

//  Qt3DCore::Quick::Quick3DEntityLoader::~Quick3DEntityLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoaderD1Ev(
    Qt3DCore::Quick::Quick3DEntityLoader *self) {
  delete self;
}

//  QObject *Qt3DCore::Quick::Quick3DEntityLoader::entity() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK8Qt3DCore5Quick19Quick3DEntityLoader6entityEv(
    const Qt3DCore::Quick::Quick3DEntityLoader *self) {
  return self->entity();
}

//  QUrl Qt3DCore::Quick::Quick3DEntityLoader::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK8Qt3DCore5Quick19Quick3DEntityLoader6sourceEv(
    const Qt3DCore::Quick::Quick3DEntityLoader *self) {
  return new QUrl(self->source());
}

//  void Qt3DCore::Quick::Quick3DEntityLoader::setSource(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader9setSourceERK4QUrl(
    Qt3DCore::Quick::Quick3DEntityLoader *self,
    const QUrl *url) {
  self->setSource(*url);
}

//  QQmlComponent *Qt3DCore::Quick::Quick3DEntityLoader::sourceComponent()
//      const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK8Qt3DCore5Quick19Quick3DEntityLoader15sourceComponentEv(
    const Qt3DCore::Quick::Quick3DEntityLoader *self) {
  return self->sourceComponent();
}

//  void
//      Qt3DCore::Quick::Quick3DEntityLoader::setSourceComponent(QQmlComponen
//      t *components)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader18setSourceComponentEP13QQmlComponent(
    Qt3DCore::Quick::Quick3DEntityLoader *self,
    QQmlComponent *components) {
  self->setSourceComponent(components);
}

//  Status Qt3DCore::Quick::Quick3DEntityLoader::status() const
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::Quick3DEntityLoader::Status ritual_ZNK8Qt3DCore5Quick19Quick3DEntityLoader6statusEv(
    const Qt3DCore::Quick::Quick3DEntityLoader *self) {
  return self->status();
}

//  void Qt3DCore::Quick::Quick3DEntityLoader::entityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader13entityChangedEv(
    Qt3DCore::Quick::Quick3DEntityLoader *self) {
  self->entityChanged();
}

//  void Qt3DCore::Quick::Quick3DEntityLoader::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader13sourceChangedEv(
    Qt3DCore::Quick::Quick3DEntityLoader *self) {
  self->sourceChanged();
}

//  void Qt3DCore::Quick::Quick3DEntityLoader::sourceComponentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader22sourceComponentChangedEv(
    Qt3DCore::Quick::Quick3DEntityLoader *self) {
  self->sourceComponentChanged();
}

//  void Qt3DCore::Quick::Quick3DEntityLoader::statusChanged(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader13statusChangedENS1_6StatusE(
    Qt3DCore::Quick::Quick3DEntityLoader *self,
    Qt3DCore::Quick::Quick3DEntityLoader::Status status) {
  self->statusChanged(status);
}

//  Quick3DEntityLoaderPrivate
//      *Qt3DCore::Quick::Quick3DEntityLoader::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::Quick3DEntityLoaderPrivate *ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader6d_funcEv(
    Qt3DCore::Quick::Quick3DEntityLoader *self) {
  return self->d_func();
}

//  const Quick3DEntityLoaderPrivate
//      *Qt3DCore::Quick::Quick3DEntityLoader::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::Quick::Quick3DEntityLoaderPrivate *ritual_ZNK8Qt3DCore5Quick19Quick3DEntityLoader6d_funcEv(
    const Qt3DCore::Quick::Quick3DEntityLoader *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DCore_Quick_Quick3DEntityLoader, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_Quick_Quick3DEntityLoader(
    Qt3DCore::Quick::Quick3DEntityLoader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_Quick_Quick3DEntityLoader *>(self)->take(key, call);
}
