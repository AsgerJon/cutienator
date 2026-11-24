//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuahistoryevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuahistoryevent.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QOpcUaHistoryEvent::QOpcUaHistoryEvent()
extern "C" Q_DECL_EXPORT
QOpcUaHistoryEvent *ritual_ZN18QOpcUaHistoryEventC1Ev() {
  return new QOpcUaHistoryEvent();
}

//  QOpcUaHistoryEvent::QOpcUaHistoryEvent(const QString &nodeId)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryEvent *ritual_ZN18QOpcUaHistoryEventC1ERK7QString(
    const QString *nodeId) {
  return new QOpcUaHistoryEvent(*nodeId);
}

//  QOpcUaHistoryEvent::QOpcUaHistoryEvent(const QOpcUaHistoryEvent &other)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryEvent *ritual_ZN18QOpcUaHistoryEventC1ERKS_(
    const QOpcUaHistoryEvent *other) {
  return new QOpcUaHistoryEvent(*other);
}

//  QOpcUaHistoryEvent::~QOpcUaHistoryEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpcUaHistoryEventD1Ev(QOpcUaHistoryEvent *self) {
  delete self;
}

//  QOpcUa::UaStatusCode QOpcUaHistoryEvent::statusCode() const
extern "C" Q_DECL_EXPORT
QOpcUa::UaStatusCode ritual_ZNK18QOpcUaHistoryEvent10statusCodeEv(
    const QOpcUaHistoryEvent *self) {
  return self->statusCode();
}

//  void QOpcUaHistoryEvent::setStatusCode(QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpcUaHistoryEvent13setStatusCodeEN6QOpcUa12UaStatusCodeE(
    QOpcUaHistoryEvent *self,
    QOpcUa::UaStatusCode statusCode) {
  self->setStatusCode(statusCode);
}

//  int QOpcUaHistoryEvent::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QOpcUaHistoryEvent5countEv(const QOpcUaHistoryEvent *self) {
  return self->count();
}

//  void QOpcUaHistoryEvent::addEvent(const QVariantList &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpcUaHistoryEvent8addEventERK5QListI8QVariantE(
    QOpcUaHistoryEvent *self,
    const QList<QVariant> *value) {
  self->addEvent(*value);
}

//  QString QOpcUaHistoryEvent::nodeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QOpcUaHistoryEvent6nodeIdEv(
    const QOpcUaHistoryEvent *self) {
  return new QString(self->nodeId());
}

//  void QOpcUaHistoryEvent::setNodeId(const QString &nodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpcUaHistoryEvent9setNodeIdERK7QString(
    QOpcUaHistoryEvent *self,
    const QString *nodeId) {
  self->setNodeId(*nodeId);
}

//  bool operator==(const QOpcUaHistoryEvent &lhs, const QOpcUaHistoryEvent
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QOpcUaHistoryEventS1_(
    const QOpcUaHistoryEvent *lhs,
    const QOpcUaHistoryEvent *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaHistoryEvent &lhs, const QOpcUaHistoryEvent
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QOpcUaHistoryEventS1_(
    const QOpcUaHistoryEvent *lhs,
    const QOpcUaHistoryEvent *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QList<QOpcUaHistoryEvent>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaHistoryEvent> *ritual_list_make_QOpcUaHistoryEvent() {
  return new QList<QOpcUaHistoryEvent>();
}

//  void QList<QOpcUaHistoryEvent>::append(const QOpcUaHistoryEvent &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaHistoryEvent(
    QList<QOpcUaHistoryEvent> *self,
    const QOpcUaHistoryEvent *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaHistoryEvent>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaHistoryEvent(
    const QList<QOpcUaHistoryEvent> *self) {
  return self->size();
}

//  const QOpcUaHistoryEvent &QList<QOpcUaHistoryEvent>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QOpcUaHistoryEvent *ritual_list_at_QOpcUaHistoryEvent(
    const QList<QOpcUaHistoryEvent> *self,
    long long index) {
  return new QOpcUaHistoryEvent(self->at(index));
}

//  QList<QOpcUaHistoryEvent>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaHistoryEvent(QList<QOpcUaHistoryEvent> *self) {
  delete self;
}
