//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/metadatabase_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/metadatabase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qobject.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A qdesigner_internal::MetaDataBase that Python can take functions over in. Every qdesigner_internal::MetaDataBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*Cuteqdesigner_internal_MetaDataBaseCall0)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_MetaDataBaseCall1)(const void *, QObject *, int *);
typedef void * (*Cuteqdesigner_internal_MetaDataBaseCall2)(const void *, QObject *, int *);
typedef void (*Cuteqdesigner_internal_MetaDataBaseCall3)(const void *, QObject *, int *);
typedef void (*Cuteqdesigner_internal_MetaDataBaseCall4)(const void *, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_MetaDataBaseCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_MetaDataBaseCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_MetaDataBaseCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_MetaDataBaseCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_MetaDataBaseCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_MetaDataBaseCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_MetaDataBaseCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cuteqdesigner_internal_MetaDataBase : public qdesigner_internal::MetaDataBase {
public:
  using qdesigner_internal::MetaDataBase::MetaDataBase;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK30QDesignerMetaDataBaseInterface4coreEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerMetaDataBaseInterface4itemEP7QObject")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18qdesigner_internal12MetaDataBase16metaDataBaseItemEP7QObject")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QDesignerMetaDataBaseInterface3addEP7QObject")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QDesignerMetaDataBaseInterface6removeEP7QObject")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QDesignerFormEditorInterface
  //      *qdesigner_internal::MetaDataBase::core() const
  QDesignerFormEditorInterface *core() const override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_MetaDataBaseCall0 call = reinterpret_cast<Cuteqdesigner_internal_MetaDataBaseCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormEditorInterface *>(given);
    }
    return qdesigner_internal::MetaDataBase::core();
  }

  //  QDesignerMetaDataBaseItemInterface
  //      *qdesigner_internal::MetaDataBase::item(QObject *object) const
  QDesignerMetaDataBaseItemInterface *item(QObject *object) const override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_MetaDataBaseCall1 call = reinterpret_cast<Cuteqdesigner_internal_MetaDataBaseCall1>(taken[1]);
      void * given = call(this, object, &handled);
      if (handled) return static_cast<QDesignerMetaDataBaseItemInterface *>(given);
    }
    return qdesigner_internal::MetaDataBase::item(object);
  }

  //  MetaDataBaseItem
  //      *qdesigner_internal::MetaDataBase::metaDataBaseItem(QObject
  //      *object) const
  qdesigner_internal::MetaDataBaseItem *metaDataBaseItem(
      QObject *object) const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_MetaDataBaseCall2 call = reinterpret_cast<Cuteqdesigner_internal_MetaDataBaseCall2>(taken[2]);
      void * given = call(this, object, &handled);
      if (handled) return static_cast<qdesigner_internal::MetaDataBaseItem *>(given);
    }
    return qdesigner_internal::MetaDataBase::metaDataBaseItem(object);
  }

  //  void qdesigner_internal::MetaDataBase::add(QObject *object)
  void add(QObject *object) override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_MetaDataBaseCall3 call = reinterpret_cast<Cuteqdesigner_internal_MetaDataBaseCall3>(taken[3]);
      call(this, object, &handled);
      if (handled) return;
    }
    qdesigner_internal::MetaDataBase::add(object);
  }

  //  void qdesigner_internal::MetaDataBase::remove(QObject *object)
  void remove(QObject *object) override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_MetaDataBaseCall4 call = reinterpret_cast<Cuteqdesigner_internal_MetaDataBaseCall4>(taken[4]);
      call(this, object, &handled);
      if (handled) return;
    }
    qdesigner_internal::MetaDataBase::remove(object);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_MetaDataBaseCall5 call = reinterpret_cast<Cuteqdesigner_internal_MetaDataBaseCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_MetaDataBaseCall6 call = reinterpret_cast<Cuteqdesigner_internal_MetaDataBaseCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_MetaDataBaseCall7 call = reinterpret_cast<Cuteqdesigner_internal_MetaDataBaseCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      Cuteqdesigner_internal_MetaDataBaseCall8 call = reinterpret_cast<Cuteqdesigner_internal_MetaDataBaseCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      Cuteqdesigner_internal_MetaDataBaseCall9 call = reinterpret_cast<Cuteqdesigner_internal_MetaDataBaseCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      Cuteqdesigner_internal_MetaDataBaseCall10 call = reinterpret_cast<Cuteqdesigner_internal_MetaDataBaseCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      Cuteqdesigner_internal_MetaDataBaseCall11 call = reinterpret_cast<Cuteqdesigner_internal_MetaDataBaseCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *qdesigner_internal::MetaDataBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal12MetaDataBase10metaObjectEv(
    const qdesigner_internal::MetaDataBase *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::MetaDataBase::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal12MetaDataBase11qt_metacastEPKc(
    qdesigner_internal::MetaDataBase *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::MetaDataBase::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal12MetaDataBase11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::MetaDataBase *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::MetaDataBase::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal12MetaDataBase2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::MetaDataBase::tr(s, c, n));
}

//  qdesigner_internal::MetaDataBase::MetaDataBase(QDesignerFormEditorInterfa
//      ce *core, QObject *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::MetaDataBase *ritual_ZN18qdesigner_internal12MetaDataBaseC1EP28QDesignerFormEditorInterfaceP7QObject(
    QDesignerFormEditorInterface *core,
    QObject *parent) {
  return new Cuteqdesigner_internal_MetaDataBase(core, parent);
}

//  qdesigner_internal::MetaDataBase::~MetaDataBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12MetaDataBaseD1Ev(
    qdesigner_internal::MetaDataBase *self) {
  delete self;
}

//  QDesignerFormEditorInterface *qdesigner_internal::MetaDataBase::core()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK18qdesigner_internal12MetaDataBase4coreEv(
    const qdesigner_internal::MetaDataBase *self) {
  return self->core();
}

//  QDesignerMetaDataBaseItemInterface
//      *qdesigner_internal::MetaDataBase::item(QObject *object) const
extern "C" Q_DECL_EXPORT
QDesignerMetaDataBaseItemInterface *ritual_ZNK18qdesigner_internal12MetaDataBase4itemEP7QObject(
    const qdesigner_internal::MetaDataBase *self,
    QObject *object) {
  return self->item(object);
}

//  MetaDataBaseItem
//      *qdesigner_internal::MetaDataBase::metaDataBaseItem(QObject *object)
//      const
extern "C" Q_DECL_EXPORT
qdesigner_internal::MetaDataBaseItem *ritual_ZNK18qdesigner_internal12MetaDataBase16metaDataBaseItemEP7QObject(
    const qdesigner_internal::MetaDataBase *self,
    QObject *object) {
  return self->metaDataBaseItem(object);
}

//  void qdesigner_internal::MetaDataBase::add(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12MetaDataBase3addEP7QObject(
    qdesigner_internal::MetaDataBase *self,
    QObject *object) {
  self->add(object);
}

//  void qdesigner_internal::MetaDataBase::remove(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12MetaDataBase6removeEP7QObject(
    qdesigner_internal::MetaDataBase *self,
    QObject *object) {
  self->remove(object);
}

//  QObjectList qdesigner_internal::MetaDataBase::objects() const
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZNK18qdesigner_internal12MetaDataBase7objectsEv(
    const qdesigner_internal::MetaDataBase *self) {
  return new QList<QObject *>(self->objects());
}

//  void qdesigner_internal::MetaDataBase::slotDestroyed(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12MetaDataBase13slotDestroyedEP7QObject(
    qdesigner_internal::MetaDataBase *self,
    QObject *object) {
  self->slotDestroyed(object);
}

//  a Python function taken by a Cuteqdesigner_internal_MetaDataBase, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_MetaDataBase(
    qdesigner_internal::MetaDataBase *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_MetaDataBase *>(self)->take(key, call);
}

//  QDesignerFormEditorInterface *qdesigner_internal::MetaDataBase::core()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_own_ZNK18qdesigner_internal12MetaDataBase4coreEv(
    const qdesigner_internal::MetaDataBase *self) {
  return self->qdesigner_internal::MetaDataBase::core();
}

//  QDesignerMetaDataBaseItemInterface
//      *qdesigner_internal::MetaDataBase::item(QObject *object) const
extern "C" Q_DECL_EXPORT
QDesignerMetaDataBaseItemInterface *ritual_own_ZNK18qdesigner_internal12MetaDataBase4itemEP7QObject(
    const qdesigner_internal::MetaDataBase *self,
    QObject *object) {
  return self->qdesigner_internal::MetaDataBase::item(object);
}

//  MetaDataBaseItem
//      *qdesigner_internal::MetaDataBase::metaDataBaseItem(QObject *object)
//      const
extern "C" Q_DECL_EXPORT
qdesigner_internal::MetaDataBaseItem *ritual_own_ZNK18qdesigner_internal12MetaDataBase16metaDataBaseItemEP7QObject(
    const qdesigner_internal::MetaDataBase *self,
    QObject *object) {
  return self->qdesigner_internal::MetaDataBase::metaDataBaseItem(object);
}

//  void qdesigner_internal::MetaDataBase::add(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal12MetaDataBase3addEP7QObject(
    qdesigner_internal::MetaDataBase *self,
    QObject *object) {
  self->qdesigner_internal::MetaDataBase::add(object);
}

//  void qdesigner_internal::MetaDataBase::remove(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal12MetaDataBase6removeEP7QObject(
    qdesigner_internal::MetaDataBase *self,
    QObject *object) {
  self->qdesigner_internal::MetaDataBase::remove(object);
}
