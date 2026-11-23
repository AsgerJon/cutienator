//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobject.h>
#include <QtCore/qstring.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qobjectdefs.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QObject may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQObject : QObject {
  using QObject::timerEvent;
  using QObject::childEvent;
  using QObject::customEvent;
  using QObject::connectNotify;
  using QObject::disconnectNotify;
};

//  A QObject that Python can take functions over in. Every QObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQObjectCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQObjectCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQObjectCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQObjectCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQObjectCall4)(const void *, QEvent *, int *);
typedef void (*CuteQObjectCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQObjectCall6)(const void *, const QMetaMethod *, int *);
class CuteQObject : public QObject {
public:
  using QObject::QObject;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQObjectCall0 call = reinterpret_cast<CuteQObjectCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQObjectCall1 call = reinterpret_cast<CuteQObjectCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQObjectCall2 call = reinterpret_cast<CuteQObjectCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQObjectCall3 call = reinterpret_cast<CuteQObjectCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQObjectCall4 call = reinterpret_cast<CuteQObjectCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQObjectCall5 call = reinterpret_cast<CuteQObjectCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQObjectCall6 call = reinterpret_cast<CuteQObjectCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QObject::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QObject10metaObjectEv(const QObject *self) {
  return self->metaObject();
}

//  QString QObject::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QObject2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QObject::tr(s, c, n));
}

//  QObject::QObject(QObject *parent)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN7QObjectC1EPS_(QObject *parent) {
  return new CuteQObject(parent);
}

//  QObject::~QObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QObjectD1Ev(QObject *self) {
  delete self;
}

//  bool QObject::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QObject5eventEP6QEvent(QObject *self, QEvent *event) {
  return self->event(event);
}

//  bool QObject::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QObject11eventFilterEPS_P6QEvent(
    QObject *self,
    QObject *watched,
    QEvent *event) {
  return self->eventFilter(watched, event);
}

//  QString QObject::objectName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QObject10objectNameEv(const QObject *self) {
  return new QString(self->objectName());
}

//  void QObject::setObjectName(QAnyStringView name)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QObject13setObjectNameE14QAnyStringView(
    QObject *self,
    const QString *name) {
  self->setObjectName(QAnyStringView(*name));
}

//  bool QObject::isWidgetType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QObject12isWidgetTypeEv(const QObject *self) {
  return self->isWidgetType();
}

//  bool QObject::isWindowType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QObject12isWindowTypeEv(const QObject *self) {
  return self->isWindowType();
}

//  bool QObject::isQuickItemType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QObject15isQuickItemTypeEv(const QObject *self) {
  return self->isQuickItemType();
}

//  bool QObject::isQmlExposed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QObject12isQmlExposedEv(const QObject *self) {
  return self->isQmlExposed();
}

//  bool QObject::signalsBlocked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QObject14signalsBlockedEv(const QObject *self) {
  return self->signalsBlocked();
}

//  bool QObject::blockSignals(bool b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QObject12blockSignalsEb(QObject *self, bool b) {
  return self->blockSignals(b);
}

//  QThread *QObject::thread() const
extern "C" Q_DECL_EXPORT
QThread *ritual_ZNK7QObject6threadEv(const QObject *self) {
  return self->thread();
}

//  int QObject::startTimer(int interval, Qt::TimerType timerType)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QObject10startTimerEiN2Qt9TimerTypeE(
    QObject *self,
    int interval,
    Qt::TimerType timerType) {
  return self->startTimer(interval, timerType);
}

//  void QObject::killTimer(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QObject9killTimerEi(QObject *self, int id) {
  self->killTimer(id);
}

//  void QObject::killTimer(Qt::TimerId id)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QObject9killTimerEN2Qt7TimerIdE(
    QObject *self,
    Qt::TimerId id) {
  self->killTimer(id);
}

//  const QObjectList &QObject::children() const
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZNK7QObject8childrenEv(const QObject *self) {
  return new QList<QObject *>(self->children());
}

//  void QObject::setParent(QObject *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QObject9setParentEPS_(QObject *self, QObject *parent) {
  self->setParent(parent);
}

//  void QObject::installEventFilter(QObject *filterObj)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QObject18installEventFilterEPS_(
    QObject *self,
    QObject *filterObj) {
  self->installEventFilter(filterObj);
}

//  void QObject::removeEventFilter(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QObject17removeEventFilterEPS_(QObject *self, QObject *obj) {
  self->removeEventFilter(obj);
}

//  QMetaObject::Connection QObject::connect(const QObject *sender, const
//      char *signal, const QObject *receiver, const char *member,
//      Qt::ConnectionType a4)
extern "C" Q_DECL_EXPORT
QMetaObject::Connection *ritual_ZN7QObject7connectEPKS_PKcS1_S3_N2Qt14ConnectionTypeE(
    const QObject *sender,
    const char *signal,
    const QObject *receiver,
    const char *member,
    Qt::ConnectionType a4) {
  return new QMetaObject::Connection(
      QObject::connect(
          sender,
          signal,
          receiver,
          member,
          a4));
}

//  QMetaObject::Connection QObject::connect(const QObject *sender, const
//      QMetaMethod &signal, const QObject *receiver, const QMetaMethod
//      &method, Qt::ConnectionType type)
extern "C" Q_DECL_EXPORT
QMetaObject::Connection *ritual_ZN7QObject7connectEPKS_RK11QMetaMethodS1_S4_N2Qt14ConnectionTypeE(
    const QObject *sender,
    const QMetaMethod *signal,
    const QObject *receiver,
    const QMetaMethod *method,
    Qt::ConnectionType type) {
  return new QMetaObject::Connection(
      QObject::connect(
          sender,
          *signal,
          receiver,
          *method,
          type));
}

//  QMetaObject::Connection QObject::connect(const QObject *sender, const
//      char *signal, const char *member, Qt::ConnectionType type) const
extern "C" Q_DECL_EXPORT
QMetaObject::Connection *ritual_ZNK7QObject7connectEPKS_PKcS3_N2Qt14ConnectionTypeE(
    const QObject *self,
    const QObject *sender,
    const char *signal,
    const char *member,
    Qt::ConnectionType type) {
  return new QMetaObject::Connection(
      self->connect(
          sender,
          signal,
          member,
          type));
}

//  bool QObject::disconnect(const QObject *sender, const char *signal, const
//      QObject *receiver, const char *member)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QObject10disconnectEPKS_PKcS1_S3_(
    const QObject *sender,
    const char *signal,
    const QObject *receiver,
    const char *member) {
  return QObject::disconnect(sender, signal, receiver, member);
}

//  bool QObject::disconnect(const QObject *sender, const QMetaMethod
//      &signal, const QObject *receiver, const QMetaMethod &member)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QObject10disconnectEPKS_RK11QMetaMethodS1_S4_(
    const QObject *sender,
    const QMetaMethod *signal,
    const QObject *receiver,
    const QMetaMethod *member) {
  return QObject::disconnect(sender, *signal, receiver, *member);
}

//  bool QObject::disconnect(const char *signal, const QObject *receiver,
//      const char *member) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QObject10disconnectEPKcPKS_S1_(
    const QObject *self,
    const char *signal,
    const QObject *receiver,
    const char *member) {
  return self->disconnect(signal, receiver, member);
}

//  bool QObject::disconnect(const QObject *receiver, const char *member)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QObject10disconnectEPKS_PKc(
    const QObject *self,
    const QObject *receiver,
    const char *member) {
  return self->disconnect(receiver, member);
}

//  bool QObject::disconnect(const QMetaObject::Connection &a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QObject10disconnectERKN11QMetaObject10ConnectionE(
    const QMetaObject::Connection *a0) {
  return QObject::disconnect(*a0);
}

//  void QObject::dumpObjectTree() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK7QObject14dumpObjectTreeEv(const QObject *self) {
  self->dumpObjectTree();
}

//  void QObject::dumpObjectInfo() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK7QObject14dumpObjectInfoEv(const QObject *self) {
  self->dumpObjectInfo();
}

//  bool QObject::setProperty(const char *name, const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QObject11setPropertyEPKcRK8QVariant(
    QObject *self,
    const char *name,
    const QVariant *value) {
  return self->setProperty(name, *value);
}

//  QVariant QObject::property(const char *name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK7QObject8propertyEPKc(
    const QObject *self,
    const char *name) {
  return new QVariant(self->property(name));
}

//  QList<QByteArray> QObject::dynamicPropertyNames() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK7QObject20dynamicPropertyNamesEv(
    const QObject *self) {
  return new QList<QByteArray>(self->dynamicPropertyNames());
}

//  QBindingStorage *QObject::bindingStorage()
extern "C" Q_DECL_EXPORT
QBindingStorage *ritual_ZN7QObject14bindingStorageEv(QObject *self) {
  return self->bindingStorage();
}

//  const QBindingStorage *QObject::bindingStorage() const
extern "C" Q_DECL_EXPORT
const QBindingStorage *ritual_ZNK7QObject14bindingStorageEv(
    const QObject *self) {
  return self->bindingStorage();
}

//  QObject *QObject::parent() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK7QObject6parentEv(const QObject *self) {
  return self->parent();
}

//  bool QObject::inherits(const char *classname) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QObject8inheritsEPKc(
    const QObject *self,
    const char *classname) {
  return self->inherits(classname);
}

//  void QObject::deleteLater()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QObject11deleteLaterEv(QObject *self) {
  self->deleteLater();
}

//  QObject *QObject::sender() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK7QObject6senderEv(const QObject *self) {
  return self->sender();
}

//  int QObject::senderSignalIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QObject17senderSignalIndexEv(const QObject *self) {
  return self->senderSignalIndex();
}

//  int QObject::receivers(const char *signal) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QObject9receiversEPKc(
    const QObject *self,
    const char *signal) {
  return self->receivers(signal);
}

//  bool QObject::isSignalConnected(const QMetaMethod &signal) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QObject17isSignalConnectedERK11QMetaMethod(
    const QObject *self,
    const QMetaMethod *signal) {
  return self->isSignalConnected(*signal);
}

//  void QObject::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QObject10timerEventEP11QTimerEvent(
    QObject *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QObject::childEvent(QChildEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QObject10childEventEP11QChildEvent(
    QObject *self,
    QChildEvent *event) {
  self->childEvent(event);
}

//  void QObject::customEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QObject11customEventEP6QEvent(QObject *self, QEvent *event) {
  self->customEvent(event);
}

//  void QObject::connectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QObject13connectNotifyERK11QMetaMethod(
    QObject *self,
    const QMetaMethod *signal) {
  self->connectNotify(*signal);
}

//  void QObject::disconnectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QObject16disconnectNotifyERK11QMetaMethod(
    QObject *self,
    const QMetaMethod *signal) {
  self->disconnectNotify(*signal);
}

//  void QObject::doSetObjectName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QObject15doSetObjectNameERK7QString(
    QObject *self,
    const QString *name) {
  self->doSetObjectName(*name);
}

//  bool QObject::doSetProperty(const char *name, const QVariant &value,
//      QVariant *rvalue)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QObject13doSetPropertyEPKcRK8QVariantPS2_(
    QObject *self,
    const char *name,
    const QVariant *value,
    QVariant *rvalue) {
  return self->doSetProperty(name, *value, rvalue);
}

//  a Python function taken by a CuteQObject, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QObject(QObject *self, const char *key, void *call) {
  return static_cast<CuteQObject *>(self)->take(key, call);
}

//  bool QObject::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QObject5eventEP6QEvent(QObject *self, QEvent *event) {
  return self->QObject::event(event);
}

//  bool QObject::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QObject11eventFilterEPS_P6QEvent(
    QObject *self,
    QObject *watched,
    QEvent *event) {
  return self->QObject::eventFilter(watched, event);
}

//  void QObject::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QObject10timerEventEP11QTimerEvent(
    QObject *self,
    QTimerEvent *event) {
  static_cast<OwnQObject *>(self)->OwnQObject::timerEvent(event);
}

//  void QObject::childEvent(QChildEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QObject10childEventEP11QChildEvent(
    QObject *self,
    QChildEvent *event) {
  static_cast<OwnQObject *>(self)->OwnQObject::childEvent(event);
}

//  void QObject::customEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QObject11customEventEP6QEvent(
    QObject *self,
    QEvent *event) {
  static_cast<OwnQObject *>(self)->OwnQObject::customEvent(event);
}

//  void QObject::connectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QObject13connectNotifyERK11QMetaMethod(
    QObject *self,
    const QMetaMethod *signal) {
  static_cast<OwnQObject *>(self)->OwnQObject::connectNotify(*signal);
}

//  void QObject::disconnectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QObject16disconnectNotifyERK11QMetaMethod(
    QObject *self,
    const QMetaMethod *signal) {
  static_cast<OwnQObject *>(self)->OwnQObject::disconnectNotify(*signal);
}

//  QList<QObject *>::QList()
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_list_make_QObject_ptr() {
  return new QList<QObject *>();
}

//  void QList<QObject *>::append(const QObject * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QObject_ptr(QList<QObject *> *self, QObject *element) {
  self->append(element);
}

//  qsizetype QList<QObject *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QObject_ptr(const QList<QObject *> *self) {
  return self->size();
}

//  const QObject * &QList<QObject *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QObject *ritual_list_at_QObject_ptr(
    const QList<QObject *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QObject *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QObject_ptr(QList<QObject *> *self) {
  delete self;
}
