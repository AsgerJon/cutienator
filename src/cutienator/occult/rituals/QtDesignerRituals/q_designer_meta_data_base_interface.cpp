//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractmetadatabase.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/abstractmetadatabase.h>
#include <QtCore/qstring.h>
#include <QtCore/qobject.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerMetaDataBaseInterface that Python can take functions over in. Every QDesignerMetaDataBaseInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDesignerMetaDataBaseInterfaceCall0)(const void *, QObject *, int *);
typedef void (*CuteQDesignerMetaDataBaseInterfaceCall1)(const void *, QObject *, int *);
typedef void (*CuteQDesignerMetaDataBaseInterfaceCall2)(const void *, QObject *, int *);
typedef void * (*CuteQDesignerMetaDataBaseInterfaceCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerMetaDataBaseInterfaceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerMetaDataBaseInterfaceCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMetaDataBaseInterfaceCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMetaDataBaseInterfaceCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMetaDataBaseInterfaceCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMetaDataBaseInterfaceCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMetaDataBaseInterfaceCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerMetaDataBaseInterface : public QDesignerMetaDataBaseInterface {
public:
  using QDesignerMetaDataBaseInterface::QDesignerMetaDataBaseInterface;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK30QDesignerMetaDataBaseInterface4itemEP7QObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QDesignerMetaDataBaseInterface3addEP7QObject")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QDesignerMetaDataBaseInterface6removeEP7QObject")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerMetaDataBaseInterface4coreEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QDesignerMetaDataBaseItemInterface
  //      *QDesignerMetaDataBaseInterface::item(QObject *object) const
  QDesignerMetaDataBaseItemInterface *item(QObject *object) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerMetaDataBaseInterfaceCall0 call = reinterpret_cast<CuteQDesignerMetaDataBaseInterfaceCall0>(taken[0]);
      void * given = call(this, object, &handled);
      if (handled) return static_cast<QDesignerMetaDataBaseItemInterface *>(given);
    }
    return {};
  }

  //  void QDesignerMetaDataBaseInterface::add(QObject *object)
  void add(QObject *object) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerMetaDataBaseInterfaceCall1 call = reinterpret_cast<CuteQDesignerMetaDataBaseInterfaceCall1>(taken[1]);
      call(this, object, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerMetaDataBaseInterface::remove(QObject *object)
  void remove(QObject *object) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerMetaDataBaseInterfaceCall2 call = reinterpret_cast<CuteQDesignerMetaDataBaseInterfaceCall2>(taken[2]);
      call(this, object, &handled);
      if (handled) return;
    }
  }

  //  QDesignerFormEditorInterface *QDesignerMetaDataBaseInterface::core()
  //      const
  QDesignerFormEditorInterface *core() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerMetaDataBaseInterfaceCall3 call = reinterpret_cast<CuteQDesignerMetaDataBaseInterfaceCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormEditorInterface *>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerMetaDataBaseInterfaceCall4 call = reinterpret_cast<CuteQDesignerMetaDataBaseInterfaceCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerMetaDataBaseInterfaceCall5 call = reinterpret_cast<CuteQDesignerMetaDataBaseInterfaceCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerMetaDataBaseInterfaceCall6 call = reinterpret_cast<CuteQDesignerMetaDataBaseInterfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerMetaDataBaseInterfaceCall7 call = reinterpret_cast<CuteQDesignerMetaDataBaseInterfaceCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerMetaDataBaseInterfaceCall8 call = reinterpret_cast<CuteQDesignerMetaDataBaseInterfaceCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerMetaDataBaseInterfaceCall9 call = reinterpret_cast<CuteQDesignerMetaDataBaseInterfaceCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerMetaDataBaseInterfaceCall10 call = reinterpret_cast<CuteQDesignerMetaDataBaseInterfaceCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerMetaDataBaseInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QDesignerMetaDataBaseInterface10metaObjectEv(
    const QDesignerMetaDataBaseInterface *self) {
  return self->metaObject();
}

//  void *QDesignerMetaDataBaseInterface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN30QDesignerMetaDataBaseInterface11qt_metacastEPKc(
    QDesignerMetaDataBaseInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDesignerMetaDataBaseInterface::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN30QDesignerMetaDataBaseInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    QDesignerMetaDataBaseInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDesignerMetaDataBaseInterface::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QDesignerMetaDataBaseInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerMetaDataBaseInterface::tr(s, c, n));
}

//  QDesignerMetaDataBaseInterface::~QDesignerMetaDataBaseInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDesignerMetaDataBaseInterfaceD1Ev(
    QDesignerMetaDataBaseInterface *self) {
  delete self;
}

//  QDesignerMetaDataBaseItemInterface
//      *QDesignerMetaDataBaseInterface::item(QObject *object) const
extern "C" Q_DECL_EXPORT
QDesignerMetaDataBaseItemInterface *ritual_ZNK30QDesignerMetaDataBaseInterface4itemEP7QObject(
    const QDesignerMetaDataBaseInterface *self,
    QObject *object) {
  return self->item(object);
}

//  void QDesignerMetaDataBaseInterface::add(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDesignerMetaDataBaseInterface3addEP7QObject(
    QDesignerMetaDataBaseInterface *self,
    QObject *object) {
  self->add(object);
}

//  void QDesignerMetaDataBaseInterface::remove(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDesignerMetaDataBaseInterface6removeEP7QObject(
    QDesignerMetaDataBaseInterface *self,
    QObject *object) {
  self->remove(object);
}

//  QList<QObject *> QDesignerMetaDataBaseInterface::objects() const
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZNK30QDesignerMetaDataBaseInterface7objectsEv(
    const QDesignerMetaDataBaseInterface *self) {
  return new QList<QObject *>(self->objects());
}

//  QDesignerFormEditorInterface *QDesignerMetaDataBaseInterface::core()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK30QDesignerMetaDataBaseInterface4coreEv(
    const QDesignerMetaDataBaseInterface *self) {
  return self->core();
}

//  void QDesignerMetaDataBaseInterface::changed()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDesignerMetaDataBaseInterface7changedEv(
    QDesignerMetaDataBaseInterface *self) {
  self->changed();
}

//  a Python function taken by a CuteQDesignerMetaDataBaseInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerMetaDataBaseInterface(
    QDesignerMetaDataBaseInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerMetaDataBaseInterface *>(self)->take(key, call);
}
