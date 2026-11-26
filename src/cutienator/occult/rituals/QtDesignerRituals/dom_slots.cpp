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

//  DomSlots::DomSlots()
extern "C" Q_DECL_EXPORT
DomSlots *ritual_ZN8DomSlotsC1Ev() {
  return new DomSlots();
}

//  DomSlots::~DomSlots()
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomSlotsD1Ev(DomSlots *self) {
  delete self;
}

//  void DomSlots::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomSlots4readER16QXmlStreamReader(
    DomSlots *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomSlots::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8DomSlots5writeER16QXmlStreamWriterRK7QString(
    const DomSlots *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  QStringList DomSlots::elementSignal() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK8DomSlots13elementSignalEv(const DomSlots *self) {
  return new QList<QString>(self->elementSignal());
}

//  void DomSlots::setElementSignal(const QStringList &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomSlots16setElementSignalERK5QListI7QStringE(
    DomSlots *self,
    const QList<QString> *a) {
  self->setElementSignal(*a);
}

//  QStringList DomSlots::elementSlot() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK8DomSlots11elementSlotEv(const DomSlots *self) {
  return new QList<QString>(self->elementSlot());
}

//  void DomSlots::setElementSlot(const QStringList &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomSlots14setElementSlotERK5QListI7QStringE(
    DomSlots *self,
    const QList<QString> *a) {
  self->setElementSlot(*a);
}
