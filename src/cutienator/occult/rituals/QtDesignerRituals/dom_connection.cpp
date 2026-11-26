//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  DomConnection::DomConnection()
extern "C" Q_DECL_EXPORT
DomConnection *ritual_ZN13DomConnectionC1Ev() {
  return new DomConnection();
}

//  DomConnection::~DomConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomConnectionD1Ev(DomConnection *self) {
  delete self;
}

//  void DomConnection::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomConnection4readER16QXmlStreamReader(
    DomConnection *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomConnection::write(QXmlStreamWriter &writer, const QString
//      &tagName) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13DomConnection5writeER16QXmlStreamWriterRK7QString(
    const DomConnection *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  QString DomConnection::elementSender() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13DomConnection13elementSenderEv(
    const DomConnection *self) {
  return new QString(self->elementSender());
}

//  void DomConnection::setElementSender(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomConnection16setElementSenderERK7QString(
    DomConnection *self,
    const QString *a) {
  self->setElementSender(*a);
}

//  bool DomConnection::hasElementSender() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13DomConnection16hasElementSenderEv(
    const DomConnection *self) {
  return self->hasElementSender();
}

//  void DomConnection::clearElementSender()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomConnection18clearElementSenderEv(DomConnection *self) {
  self->clearElementSender();
}

//  QString DomConnection::elementSignal() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13DomConnection13elementSignalEv(
    const DomConnection *self) {
  return new QString(self->elementSignal());
}

//  void DomConnection::setElementSignal(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomConnection16setElementSignalERK7QString(
    DomConnection *self,
    const QString *a) {
  self->setElementSignal(*a);
}

//  bool DomConnection::hasElementSignal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13DomConnection16hasElementSignalEv(
    const DomConnection *self) {
  return self->hasElementSignal();
}

//  void DomConnection::clearElementSignal()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomConnection18clearElementSignalEv(DomConnection *self) {
  self->clearElementSignal();
}

//  QString DomConnection::elementReceiver() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13DomConnection15elementReceiverEv(
    const DomConnection *self) {
  return new QString(self->elementReceiver());
}

//  void DomConnection::setElementReceiver(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomConnection18setElementReceiverERK7QString(
    DomConnection *self,
    const QString *a) {
  self->setElementReceiver(*a);
}

//  bool DomConnection::hasElementReceiver() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13DomConnection18hasElementReceiverEv(
    const DomConnection *self) {
  return self->hasElementReceiver();
}

//  void DomConnection::clearElementReceiver()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomConnection20clearElementReceiverEv(DomConnection *self) {
  self->clearElementReceiver();
}

//  QString DomConnection::elementSlot() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13DomConnection11elementSlotEv(
    const DomConnection *self) {
  return new QString(self->elementSlot());
}

//  void DomConnection::setElementSlot(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomConnection14setElementSlotERK7QString(
    DomConnection *self,
    const QString *a) {
  self->setElementSlot(*a);
}

//  bool DomConnection::hasElementSlot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13DomConnection14hasElementSlotEv(const DomConnection *self) {
  return self->hasElementSlot();
}

//  void DomConnection::clearElementSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomConnection16clearElementSlotEv(DomConnection *self) {
  self->clearElementSlot();
}

//  DomConnectionHints *DomConnection::elementHints() const
extern "C" Q_DECL_EXPORT
DomConnectionHints *ritual_ZNK13DomConnection12elementHintsEv(
    const DomConnection *self) {
  return self->elementHints();
}

//  DomConnectionHints *DomConnection::takeElementHints()
extern "C" Q_DECL_EXPORT
DomConnectionHints *ritual_ZN13DomConnection16takeElementHintsEv(
    DomConnection *self) {
  return self->takeElementHints();
}

//  void DomConnection::setElementHints(DomConnectionHints *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomConnection15setElementHintsEP18DomConnectionHints(
    DomConnection *self,
    DomConnectionHints *a) {
  self->setElementHints(a);
}

//  bool DomConnection::hasElementHints() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13DomConnection15hasElementHintsEv(
    const DomConnection *self) {
  return self->hasElementHints();
}

//  void DomConnection::clearElementHints()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomConnection17clearElementHintsEv(DomConnection *self) {
  self->clearElementHints();
}

//  QList<DomConnection *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomConnection *> *ritual_list_make_DomConnection_ptr() {
  return new QList<DomConnection *>();
}

//  void QList<DomConnection *>::append(const DomConnection * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomConnection_ptr(
    QList<DomConnection *> *self,
    DomConnection *element) {
  self->append(element);
}

//  qsizetype QList<DomConnection *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomConnection_ptr(
    const QList<DomConnection *> *self) {
  return self->size();
}

//  const DomConnection * &QList<DomConnection *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomConnection *ritual_list_at_DomConnection_ptr(
    const QList<DomConnection *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomConnection *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomConnection_ptr(QList<DomConnection *> *self) {
  delete self;
}
