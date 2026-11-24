//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_membersheet_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_membersheet_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QDesignerMemberSheetFactory may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDesignerMemberSheetFactory : QDesignerMemberSheetFactory {
  using QDesignerMemberSheetFactory::createExtension;
};

//  A QDesignerMemberSheetFactory that Python can take functions over in. Every QDesignerMemberSheetFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDesignerMemberSheetFactoryCall0)(const void *, QObject *, const QString *, QObject *, int *);
typedef void * (*CuteQDesignerMemberSheetFactoryCall1)(const void *, QObject *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerMemberSheetFactoryCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerMemberSheetFactoryCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMemberSheetFactoryCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMemberSheetFactoryCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMemberSheetFactoryCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMemberSheetFactoryCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMemberSheetFactoryCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerMemberSheetFactory : public QDesignerMemberSheetFactory {
public:
  using QDesignerMemberSheetFactory::QDesignerMemberSheetFactory;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK17QExtensionFactory15createExtensionEP7QObjectRK7QStringS1_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QAbstractExtensionFactory9extensionEP7QObjectRK7QString")) {
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

  //  QObject *QDesignerMemberSheetFactory::createExtension(QObject
  //      *object, const QString &iid, QObject *parent) const
  QObject *createExtension(
      QObject *object,
      const QString &iid,
      QObject *parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerMemberSheetFactoryCall0 call = reinterpret_cast<CuteQDesignerMemberSheetFactoryCall0>(taken[0]);
      void * given = call(this, object, &iid, parent, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QDesignerMemberSheetFactory::createExtension(object, iid, parent);
  }

  //  QObject *QExtensionFactory::extension(QObject *object, const QString
  //      &iid) const
  QObject *extension(QObject *object, const QString &iid) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerMemberSheetFactoryCall1 call = reinterpret_cast<CuteQDesignerMemberSheetFactoryCall1>(taken[1]);
      void * given = call(this, object, &iid, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QExtensionFactory::extension(object, iid);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerMemberSheetFactoryCall2 call = reinterpret_cast<CuteQDesignerMemberSheetFactoryCall2>(taken[2]);
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
      CuteQDesignerMemberSheetFactoryCall3 call = reinterpret_cast<CuteQDesignerMemberSheetFactoryCall3>(taken[3]);
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
      CuteQDesignerMemberSheetFactoryCall4 call = reinterpret_cast<CuteQDesignerMemberSheetFactoryCall4>(taken[4]);
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
      CuteQDesignerMemberSheetFactoryCall5 call = reinterpret_cast<CuteQDesignerMemberSheetFactoryCall5>(taken[5]);
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
      CuteQDesignerMemberSheetFactoryCall6 call = reinterpret_cast<CuteQDesignerMemberSheetFactoryCall6>(taken[6]);
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
      CuteQDesignerMemberSheetFactoryCall7 call = reinterpret_cast<CuteQDesignerMemberSheetFactoryCall7>(taken[7]);
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
      CuteQDesignerMemberSheetFactoryCall8 call = reinterpret_cast<CuteQDesignerMemberSheetFactoryCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerMemberSheetFactory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QDesignerMemberSheetFactory10metaObjectEv(
    const QDesignerMemberSheetFactory *self) {
  return self->metaObject();
}

//  QString QDesignerMemberSheetFactory::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QDesignerMemberSheetFactory2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerMemberSheetFactory::tr(s, c, n));
}

//  QDesignerMemberSheetFactory::QDesignerMemberSheetFactory(QExtensionManage
//      r *parent)
extern "C" Q_DECL_EXPORT
QDesignerMemberSheetFactory *ritual_ZN27QDesignerMemberSheetFactoryC1EP17QExtensionManager(
    QExtensionManager *parent) {
  return new CuteQDesignerMemberSheetFactory(parent);
}

//  QObject *QDesignerMemberSheetFactory::createExtension(QObject *object,
//      const QString &iid, QObject *parent) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK27QDesignerMemberSheetFactory15createExtensionEP7QObjectRK7QStringS1_(
    const QDesignerMemberSheetFactory *self,
    QObject *object,
    const QString *iid,
    QObject *parent) {
  return self->createExtension(object, *iid, parent);
}

//  a Python function taken by a CuteQDesignerMemberSheetFactory, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerMemberSheetFactory(
    QDesignerMemberSheetFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerMemberSheetFactory *>(self)->take(key, call);
}

//  QObject *QDesignerMemberSheetFactory::createExtension(QObject *object,
//      const QString &iid, QObject *parent) const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK27QDesignerMemberSheetFactory15createExtensionEP7QObjectRK7QStringS1_(
    const QDesignerMemberSheetFactory *self,
    QObject *object,
    const QString *iid,
    QObject *parent) {
  return static_cast<const OwnQDesignerMemberSheetFactory *>(self)->OwnQDesignerMemberSheetFactory::createExtension(
      object,
      *iid,
      parent);
}
