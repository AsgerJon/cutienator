//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/qscxmlevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtScxml/qscxmlevent.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>

//  QScxmlEvent::QScxmlEvent()
extern "C" Q_DECL_EXPORT
QScxmlEvent *ritual_ZN11QScxmlEventC1Ev() {
  return new QScxmlEvent();
}

//  QScxmlEvent::~QScxmlEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScxmlEventD1Ev(QScxmlEvent *self) {
  delete self;
}

//  QScxmlEvent &QScxmlEvent::operator=(const QScxmlEvent &other)
extern "C" Q_DECL_EXPORT
QScxmlEvent *ritual_ZN11QScxmlEventaSERKS_(
    QScxmlEvent *self,
    const QScxmlEvent *other) {
  return &(self->operator=(*other));
}

//  QScxmlEvent::QScxmlEvent(const QScxmlEvent &other)
extern "C" Q_DECL_EXPORT
QScxmlEvent *ritual_ZN11QScxmlEventC1ERKS_(const QScxmlEvent *other) {
  return new QScxmlEvent(*other);
}

//  QString QScxmlEvent::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QScxmlEvent4nameEv(const QScxmlEvent *self) {
  return new QString(self->name());
}

//  void QScxmlEvent::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScxmlEvent7setNameERK7QString(
    QScxmlEvent *self,
    const QString *name) {
  self->setName(*name);
}

//  EventType QScxmlEvent::eventType() const
extern "C" Q_DECL_EXPORT
QScxmlEvent::EventType ritual_ZNK11QScxmlEvent9eventTypeEv(
    const QScxmlEvent *self) {
  return self->eventType();
}

//  void QScxmlEvent::setEventType(const EventType &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScxmlEvent12setEventTypeERKNS_9EventTypeE(
    QScxmlEvent *self,
    const QScxmlEvent::EventType *type) {
  self->setEventType(*type);
}

//  QString QScxmlEvent::scxmlType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QScxmlEvent9scxmlTypeEv(const QScxmlEvent *self) {
  return new QString(self->scxmlType());
}

//  QString QScxmlEvent::sendId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QScxmlEvent6sendIdEv(const QScxmlEvent *self) {
  return new QString(self->sendId());
}

//  void QScxmlEvent::setSendId(const QString &sendId)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScxmlEvent9setSendIdERK7QString(
    QScxmlEvent *self,
    const QString *sendId) {
  self->setSendId(*sendId);
}

//  QString QScxmlEvent::origin() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QScxmlEvent6originEv(const QScxmlEvent *self) {
  return new QString(self->origin());
}

//  void QScxmlEvent::setOrigin(const QString &origin)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScxmlEvent9setOriginERK7QString(
    QScxmlEvent *self,
    const QString *origin) {
  self->setOrigin(*origin);
}

//  QString QScxmlEvent::originType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QScxmlEvent10originTypeEv(const QScxmlEvent *self) {
  return new QString(self->originType());
}

//  void QScxmlEvent::setOriginType(const QString &originType)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScxmlEvent13setOriginTypeERK7QString(
    QScxmlEvent *self,
    const QString *originType) {
  self->setOriginType(*originType);
}

//  QString QScxmlEvent::invokeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QScxmlEvent8invokeIdEv(const QScxmlEvent *self) {
  return new QString(self->invokeId());
}

//  void QScxmlEvent::setInvokeId(const QString &invokeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScxmlEvent11setInvokeIdERK7QString(
    QScxmlEvent *self,
    const QString *invokeId) {
  self->setInvokeId(*invokeId);
}

//  int QScxmlEvent::delay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QScxmlEvent5delayEv(const QScxmlEvent *self) {
  return self->delay();
}

//  void QScxmlEvent::setDelay(int delayInMiliSecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScxmlEvent8setDelayEi(
    QScxmlEvent *self,
    int delayInMiliSecs) {
  self->setDelay(delayInMiliSecs);
}

//  void QScxmlEvent::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScxmlEvent5clearEv(QScxmlEvent *self) {
  self->clear();
}

//  QVariant QScxmlEvent::data() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QScxmlEvent4dataEv(const QScxmlEvent *self) {
  return new QVariant(self->data());
}

//  void QScxmlEvent::setData(const QVariant &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScxmlEvent7setDataERK8QVariant(
    QScxmlEvent *self,
    const QVariant *data) {
  self->setData(*data);
}

//  bool QScxmlEvent::isErrorEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QScxmlEvent12isErrorEventEv(const QScxmlEvent *self) {
  return self->isErrorEvent();
}

//  QString QScxmlEvent::errorMessage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QScxmlEvent12errorMessageEv(const QScxmlEvent *self) {
  return new QString(self->errorMessage());
}

//  void QScxmlEvent::setErrorMessage(const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScxmlEvent15setErrorMessageERK7QString(
    QScxmlEvent *self,
    const QString *message) {
  self->setErrorMessage(*message);
}
