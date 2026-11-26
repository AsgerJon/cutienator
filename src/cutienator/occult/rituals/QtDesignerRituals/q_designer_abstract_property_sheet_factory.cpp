//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_propertysheet_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_propertysheet_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDesignerAbstractPropertySheetFactory that Python can take functions over in. Every QDesignerAbstractPropertySheetFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDesignerAbstractPropertySheetFactoryCall0)(const void *, QObject *, const QString *, int *);
typedef void * (*CuteQDesignerAbstractPropertySheetFactoryCall1)(const void *, QObject *, QObject *, int *);
typedef void * (*CuteQDesignerAbstractPropertySheetFactoryCall2)(const void *, QObject *, const QString *, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerAbstractPropertySheetFactoryCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerAbstractPropertySheetFactoryCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerAbstractPropertySheetFactoryCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerAbstractPropertySheetFactoryCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerAbstractPropertySheetFactoryCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerAbstractPropertySheetFactoryCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerAbstractPropertySheetFactoryCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerAbstractPropertySheetFactory : public QDesignerAbstractPropertySheetFactory {
public:
  using QDesignerAbstractPropertySheetFactory::QDesignerAbstractPropertySheetFactory;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK25QAbstractExtensionFactory9extensionEP7QObjectRK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK37QDesignerAbstractPropertySheetFactory19createPropertySheetEP7QObjectS1_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QExtensionFactory15createExtensionEP7QObjectRK7QStringS1_")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QObject *QDesignerAbstractPropertySheetFactory::extension(QObject
  //      *object, const QString &iid) const
  QObject *extension(QObject *object, const QString &iid) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerAbstractPropertySheetFactoryCall0 call = reinterpret_cast<CuteQDesignerAbstractPropertySheetFactoryCall0>(taken[0]);
      void * given = call(this, object, &iid, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QDesignerAbstractPropertySheetFactory::extension(object, iid);
  }

  //  QObject
  //      *QDesignerAbstractPropertySheetFactory::createPropertySheet(QObje
  //      ct *qObject, QObject *parent) const
  QObject *createPropertySheet(
      QObject *qObject,
      QObject *parent) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerAbstractPropertySheetFactoryCall1 call = reinterpret_cast<CuteQDesignerAbstractPropertySheetFactoryCall1>(taken[1]);
      void * given = call(this, qObject, parent, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return {};
  }

  //  QObject *QExtensionFactory::createExtension(QObject *object, const
  //      QString &iid, QObject *parent) const
  QObject *createExtension(
      QObject *object,
      const QString &iid,
      QObject *parent) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerAbstractPropertySheetFactoryCall2 call = reinterpret_cast<CuteQDesignerAbstractPropertySheetFactoryCall2>(taken[2]);
      void * given = call(this, object, &iid, parent, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QExtensionFactory::createExtension(object, iid, parent);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerAbstractPropertySheetFactoryCall3 call = reinterpret_cast<CuteQDesignerAbstractPropertySheetFactoryCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerAbstractPropertySheetFactoryCall4 call = reinterpret_cast<CuteQDesignerAbstractPropertySheetFactoryCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerAbstractPropertySheetFactoryCall5 call = reinterpret_cast<CuteQDesignerAbstractPropertySheetFactoryCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerAbstractPropertySheetFactoryCall6 call = reinterpret_cast<CuteQDesignerAbstractPropertySheetFactoryCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerAbstractPropertySheetFactoryCall7 call = reinterpret_cast<CuteQDesignerAbstractPropertySheetFactoryCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerAbstractPropertySheetFactoryCall8 call = reinterpret_cast<CuteQDesignerAbstractPropertySheetFactoryCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerAbstractPropertySheetFactoryCall9 call = reinterpret_cast<CuteQDesignerAbstractPropertySheetFactoryCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerAbstractPropertySheetFactory::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK37QDesignerAbstractPropertySheetFactory10metaObjectEv(
    const QDesignerAbstractPropertySheetFactory *self) {
  return self->metaObject();
}

//  void *QDesignerAbstractPropertySheetFactory::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN37QDesignerAbstractPropertySheetFactory11qt_metacastEPKc(
    QDesignerAbstractPropertySheetFactory *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDesignerAbstractPropertySheetFactory::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN37QDesignerAbstractPropertySheetFactory11qt_metacallEN11QMetaObject4CallEiPPv(
    QDesignerAbstractPropertySheetFactory *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDesignerAbstractPropertySheetFactory::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN37QDesignerAbstractPropertySheetFactory2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerAbstractPropertySheetFactory::tr(s, c, n));
}

//  QDesignerAbstractPropertySheetFactory::QDesignerAbstractPropertySheetFact
//      ory(QExtensionManager *parent)
extern "C" Q_DECL_EXPORT
QDesignerAbstractPropertySheetFactory *ritual_ZN37QDesignerAbstractPropertySheetFactoryC1EP17QExtensionManager(
    QExtensionManager *parent) {
  return new CuteQDesignerAbstractPropertySheetFactory(parent);
}

//  QDesignerAbstractPropertySheetFactory::~QDesignerAbstractPropertySheetFac
//      tory()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QDesignerAbstractPropertySheetFactoryD1Ev(
    QDesignerAbstractPropertySheetFactory *self) {
  delete self;
}

//  QObject *QDesignerAbstractPropertySheetFactory::extension(QObject
//      *object, const QString &iid) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK37QDesignerAbstractPropertySheetFactory9extensionEP7QObjectRK7QString(
    const QDesignerAbstractPropertySheetFactory *self,
    QObject *object,
    const QString *iid) {
  return self->extension(object, *iid);
}

//  void QDesignerAbstractPropertySheetFactory::objectDestroyed(QObject
//      *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN37QDesignerAbstractPropertySheetFactory15objectDestroyedEP7QObject(
    QDesignerAbstractPropertySheetFactory *self,
    QObject *object) {
  self->objectDestroyed(object);
}

//  QObject
//      *QDesignerAbstractPropertySheetFactory::createPropertySheet(QObject
//      *qObject, QObject *parent) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK37QDesignerAbstractPropertySheetFactory19createPropertySheetEP7QObjectS1_(
    const QDesignerAbstractPropertySheetFactory *self,
    QObject *qObject,
    QObject *parent) {
  return self->createPropertySheet(qObject, parent);
}

//  a Python function taken by a CuteQDesignerAbstractPropertySheetFactory,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerAbstractPropertySheetFactory(
    QDesignerAbstractPropertySheetFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerAbstractPropertySheetFactory *>(self)->take(key, call);
}

//  QObject *QDesignerAbstractPropertySheetFactory::extension(QObject
//      *object, const QString &iid) const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK37QDesignerAbstractPropertySheetFactory9extensionEP7QObjectRK7QString(
    const QDesignerAbstractPropertySheetFactory *self,
    QObject *object,
    const QString *iid) {
  return self->QDesignerAbstractPropertySheetFactory::extension(
      object,
      *iid);
}
