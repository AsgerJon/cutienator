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

//  DomTabStops::DomTabStops()
extern "C" Q_DECL_EXPORT
DomTabStops *ritual_ZN11DomTabStopsC1Ev() {
  return new DomTabStops();
}

//  DomTabStops::~DomTabStops()
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomTabStopsD1Ev(DomTabStops *self) {
  delete self;
}

//  void DomTabStops::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomTabStops4readER16QXmlStreamReader(
    DomTabStops *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomTabStops::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11DomTabStops5writeER16QXmlStreamWriterRK7QString(
    const DomTabStops *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  QStringList DomTabStops::elementTabStop() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11DomTabStops14elementTabStopEv(
    const DomTabStops *self) {
  return new QList<QString>(self->elementTabStop());
}

//  void DomTabStops::setElementTabStop(const QStringList &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomTabStops17setElementTabStopERK5QListI7QStringE(
    DomTabStops *self,
    const QList<QString> *a) {
  self->setElementTabStop(*a);
}
