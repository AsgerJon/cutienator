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

//  DomConnectionHints::DomConnectionHints()
extern "C" Q_DECL_EXPORT
DomConnectionHints *ritual_ZN18DomConnectionHintsC1Ev() {
  return new DomConnectionHints();
}

//  DomConnectionHints::~DomConnectionHints()
extern "C" Q_DECL_EXPORT
void ritual_ZN18DomConnectionHintsD1Ev(DomConnectionHints *self) {
  delete self;
}

//  void DomConnectionHints::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN18DomConnectionHints4readER16QXmlStreamReader(
    DomConnectionHints *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomConnectionHints::write(QXmlStreamWriter &writer, const QString
//      &tagName) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18DomConnectionHints5writeER16QXmlStreamWriterRK7QString(
    const DomConnectionHints *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  QList<DomConnectionHint *> DomConnectionHints::elementHint() const
extern "C" Q_DECL_EXPORT
QList<DomConnectionHint *> *ritual_ZNK18DomConnectionHints11elementHintEv(
    const DomConnectionHints *self) {
  return new QList<DomConnectionHint *>(self->elementHint());
}

//  void DomConnectionHints::setElementHint(const QList<DomConnectionHint *>
//      &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN18DomConnectionHints14setElementHintERK5QListIP17DomConnectionHintE(
    DomConnectionHints *self,
    const QList<DomConnectionHint *> *a) {
  self->setElementHint(*a);
}
