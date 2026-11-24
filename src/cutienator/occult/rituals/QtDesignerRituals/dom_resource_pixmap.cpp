//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  DomResourcePixmap::DomResourcePixmap()
extern "C" Q_DECL_EXPORT
DomResourcePixmap *ritual_ZN17DomResourcePixmapC1Ev() {
  return new DomResourcePixmap();
}

//  DomResourcePixmap::~DomResourcePixmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomResourcePixmapD1Ev(DomResourcePixmap *self) {
  delete self;
}

//  QString DomResourcePixmap::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17DomResourcePixmap4textEv(
    const DomResourcePixmap *self) {
  return new QString(self->text());
}

//  void DomResourcePixmap::setText(const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomResourcePixmap7setTextERK7QString(
    DomResourcePixmap *self,
    const QString *s) {
  self->setText(*s);
}

//  bool DomResourcePixmap::hasAttributeResource() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17DomResourcePixmap20hasAttributeResourceEv(
    const DomResourcePixmap *self) {
  return self->hasAttributeResource();
}

//  QString DomResourcePixmap::attributeResource() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17DomResourcePixmap17attributeResourceEv(
    const DomResourcePixmap *self) {
  return new QString(self->attributeResource());
}

//  void DomResourcePixmap::setAttributeResource(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomResourcePixmap20setAttributeResourceERK7QString(
    DomResourcePixmap *self,
    const QString *a) {
  self->setAttributeResource(*a);
}

//  void DomResourcePixmap::clearAttributeResource()
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomResourcePixmap22clearAttributeResourceEv(
    DomResourcePixmap *self) {
  self->clearAttributeResource();
}

//  bool DomResourcePixmap::hasAttributeAlias() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17DomResourcePixmap17hasAttributeAliasEv(
    const DomResourcePixmap *self) {
  return self->hasAttributeAlias();
}

//  QString DomResourcePixmap::attributeAlias() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17DomResourcePixmap14attributeAliasEv(
    const DomResourcePixmap *self) {
  return new QString(self->attributeAlias());
}

//  void DomResourcePixmap::setAttributeAlias(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomResourcePixmap17setAttributeAliasERK7QString(
    DomResourcePixmap *self,
    const QString *a) {
  self->setAttributeAlias(*a);
}

//  void DomResourcePixmap::clearAttributeAlias()
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomResourcePixmap19clearAttributeAliasEv(
    DomResourcePixmap *self) {
  self->clearAttributeAlias();
}
