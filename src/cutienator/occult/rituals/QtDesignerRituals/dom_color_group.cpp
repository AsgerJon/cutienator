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

//  DomColorGroup::DomColorGroup()
extern "C" Q_DECL_EXPORT
DomColorGroup *ritual_ZN13DomColorGroupC1Ev() {
  return new DomColorGroup();
}

//  DomColorGroup::~DomColorGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomColorGroupD1Ev(DomColorGroup *self) {
  delete self;
}

//  void DomColorGroup::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomColorGroup4readER16QXmlStreamReader(
    DomColorGroup *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomColorGroup::write(QXmlStreamWriter &writer, const QString
//      &tagName) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13DomColorGroup5writeER16QXmlStreamWriterRK7QString(
    const DomColorGroup *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  QList<DomColorRole *> DomColorGroup::elementColorRole() const
extern "C" Q_DECL_EXPORT
QList<DomColorRole *> *ritual_ZNK13DomColorGroup16elementColorRoleEv(
    const DomColorGroup *self) {
  return new QList<DomColorRole *>(self->elementColorRole());
}

//  void DomColorGroup::setElementColorRole(const QList<DomColorRole *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomColorGroup19setElementColorRoleERK5QListIP12DomColorRoleE(
    DomColorGroup *self,
    const QList<DomColorRole *> *a) {
  self->setElementColorRole(*a);
}

//  QList<DomColor *> DomColorGroup::elementColor() const
extern "C" Q_DECL_EXPORT
QList<DomColor *> *ritual_ZNK13DomColorGroup12elementColorEv(
    const DomColorGroup *self) {
  return new QList<DomColor *>(self->elementColor());
}

//  void DomColorGroup::setElementColor(const QList<DomColor *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomColorGroup15setElementColorERK5QListIP8DomColorE(
    DomColorGroup *self,
    const QList<DomColor *> *a) {
  self->setElementColor(*a);
}
