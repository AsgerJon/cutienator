//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobject.h>

//  const QMetaObject *QObject::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QObject10metaObjectEv(const QObject *self) {
  return self->metaObject();
}

//  QObject::QObject(QObject *parent)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN7QObjectC1EPS_(QObject *parent) {
  return new QObject(parent);
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

//  bool QObject::disconnect(const QObject *sender, const char *signal,
//      const QObject *receiver, const char *member)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QObject10disconnectEPKS_PKcS1_S3_(
    const QObject *sender,
    const char *signal,
    const QObject *receiver,
    const char *member) {
  return QObject::disconnect(sender, signal, receiver, member);
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
