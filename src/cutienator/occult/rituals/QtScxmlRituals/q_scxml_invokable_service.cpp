//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/qscxmlinvokableservice.h, Qt 6.12.0. Changes made here are lost.
#include <QtScxml/qscxmlinvokableservice.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QScxmlInvokableService that Python can take functions over in. Every QScxmlInvokableService
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQScxmlInvokableServiceCall0)(const void *, int *);
typedef QString * (*CuteQScxmlInvokableServiceCall1)(const void *, int *);
typedef QString * (*CuteQScxmlInvokableServiceCall2)(const void *, int *);
typedef void (*CuteQScxmlInvokableServiceCall3)(const void *, QScxmlEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlInvokableServiceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlInvokableServiceCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInvokableServiceCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInvokableServiceCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInvokableServiceCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInvokableServiceCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInvokableServiceCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScxmlInvokableService : public QScxmlInvokableService {
public:
  using QScxmlInvokableService::QScxmlInvokableService;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QScxmlInvokableService5startEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QScxmlInvokableService2idEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QScxmlInvokableService4nameEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QScxmlInvokableService9postEventEP11QScxmlEvent")) {
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

  //  bool QScxmlInvokableService::start()
  bool start() override {
    if (taken[0]) {
      int handled = 0;
      CuteQScxmlInvokableServiceCall0 call = reinterpret_cast<CuteQScxmlInvokableServiceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QScxmlInvokableService::id() const
  QString id() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQScxmlInvokableServiceCall1 call = reinterpret_cast<CuteQScxmlInvokableServiceCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QScxmlInvokableService::name() const
  QString name() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQScxmlInvokableServiceCall2 call = reinterpret_cast<CuteQScxmlInvokableServiceCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QScxmlInvokableService::postEvent(QScxmlEvent *event)
  void postEvent(QScxmlEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQScxmlInvokableServiceCall3 call = reinterpret_cast<CuteQScxmlInvokableServiceCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQScxmlInvokableServiceCall4 call = reinterpret_cast<CuteQScxmlInvokableServiceCall4>(taken[4]);
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
      CuteQScxmlInvokableServiceCall5 call = reinterpret_cast<CuteQScxmlInvokableServiceCall5>(taken[5]);
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
      CuteQScxmlInvokableServiceCall6 call = reinterpret_cast<CuteQScxmlInvokableServiceCall6>(taken[6]);
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
      CuteQScxmlInvokableServiceCall7 call = reinterpret_cast<CuteQScxmlInvokableServiceCall7>(taken[7]);
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
      CuteQScxmlInvokableServiceCall8 call = reinterpret_cast<CuteQScxmlInvokableServiceCall8>(taken[8]);
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
      CuteQScxmlInvokableServiceCall9 call = reinterpret_cast<CuteQScxmlInvokableServiceCall9>(taken[9]);
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
      CuteQScxmlInvokableServiceCall10 call = reinterpret_cast<CuteQScxmlInvokableServiceCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScxmlInvokableService::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QScxmlInvokableService10metaObjectEv(
    const QScxmlInvokableService *self) {
  return self->metaObject();
}

//  QString QScxmlInvokableService::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QScxmlInvokableService2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScxmlInvokableService::tr(s, c, n));
}

//  QScxmlInvokableServicePrivate *QScxmlInvokableService::d_func()
extern "C" Q_DECL_EXPORT
QScxmlInvokableServicePrivate *ritual_ZN22QScxmlInvokableService6d_funcEv(
    QScxmlInvokableService *self) {
  return self->d_func();
}

//  const QScxmlInvokableServicePrivate *QScxmlInvokableService::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QScxmlInvokableServicePrivate *ritual_ZNK22QScxmlInvokableService6d_funcEv(
    const QScxmlInvokableService *self) {
  return self->d_func();
}

//  QScxmlStateMachine *QScxmlInvokableService::parentStateMachine() const
extern "C" Q_DECL_EXPORT
QScxmlStateMachine *ritual_ZNK22QScxmlInvokableService18parentStateMachineEv(
    const QScxmlInvokableService *self) {
  return self->parentStateMachine();
}

//  bool QScxmlInvokableService::start()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QScxmlInvokableService5startEv(
    QScxmlInvokableService *self) {
  return self->start();
}

//  QString QScxmlInvokableService::id() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QScxmlInvokableService2idEv(
    const QScxmlInvokableService *self) {
  return new QString(self->id());
}

//  QString QScxmlInvokableService::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QScxmlInvokableService4nameEv(
    const QScxmlInvokableService *self) {
  return new QString(self->name());
}

//  void QScxmlInvokableService::postEvent(QScxmlEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QScxmlInvokableService9postEventEP11QScxmlEvent(
    QScxmlInvokableService *self,
    QScxmlEvent *event) {
  self->postEvent(event);
}

//  a Python function taken by a CuteQScxmlInvokableService, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScxmlInvokableService(
    QScxmlInvokableService *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScxmlInvokableService *>(self)->take(key, call);
}

//  QList<QScxmlInvokableService *>::QList()
extern "C" Q_DECL_EXPORT
QList<QScxmlInvokableService *> *ritual_list_make_QScxmlInvokableService_ptr() {
  return new QList<QScxmlInvokableService *>();
}

//  void QList<QScxmlInvokableService *>::append(const QScxmlInvokableService
//      * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QScxmlInvokableService_ptr(
    QList<QScxmlInvokableService *> *self,
    QScxmlInvokableService *element) {
  self->append(element);
}

//  qsizetype QList<QScxmlInvokableService *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QScxmlInvokableService_ptr(
    const QList<QScxmlInvokableService *> *self) {
  return self->size();
}

//  const QScxmlInvokableService * &QList<QScxmlInvokableService
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QScxmlInvokableService *ritual_list_at_QScxmlInvokableService_ptr(
    const QList<QScxmlInvokableService *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QScxmlInvokableService *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QScxmlInvokableService_ptr(
    QList<QScxmlInvokableService *> *self) {
  delete self;
}
