//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  DomString::DomString()
extern "C" Q_DECL_EXPORT
DomString *ritual_ZN9DomStringC1Ev() {
  return new DomString();
}

//  DomString::~DomString()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomStringD1Ev(DomString *self) {
  delete self;
}

//  QString DomString::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9DomString4textEv(const DomString *self) {
  return new QString(self->text());
}

//  void DomString::setText(const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomString7setTextERK7QString(
    DomString *self,
    const QString *s) {
  self->setText(*s);
}

//  bool DomString::hasAttributeNotr() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9DomString16hasAttributeNotrEv(const DomString *self) {
  return self->hasAttributeNotr();
}

//  QString DomString::attributeNotr() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9DomString13attributeNotrEv(const DomString *self) {
  return new QString(self->attributeNotr());
}

//  void DomString::setAttributeNotr(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomString16setAttributeNotrERK7QString(
    DomString *self,
    const QString *a) {
  self->setAttributeNotr(*a);
}

//  void DomString::clearAttributeNotr()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomString18clearAttributeNotrEv(DomString *self) {
  self->clearAttributeNotr();
}

//  bool DomString::hasAttributeComment() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9DomString19hasAttributeCommentEv(const DomString *self) {
  return self->hasAttributeComment();
}

//  QString DomString::attributeComment() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9DomString16attributeCommentEv(const DomString *self) {
  return new QString(self->attributeComment());
}

//  void DomString::setAttributeComment(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomString19setAttributeCommentERK7QString(
    DomString *self,
    const QString *a) {
  self->setAttributeComment(*a);
}

//  void DomString::clearAttributeComment()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomString21clearAttributeCommentEv(DomString *self) {
  self->clearAttributeComment();
}

//  bool DomString::hasAttributeExtraComment() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9DomString24hasAttributeExtraCommentEv(
    const DomString *self) {
  return self->hasAttributeExtraComment();
}

//  QString DomString::attributeExtraComment() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9DomString21attributeExtraCommentEv(
    const DomString *self) {
  return new QString(self->attributeExtraComment());
}

//  void DomString::setAttributeExtraComment(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomString24setAttributeExtraCommentERK7QString(
    DomString *self,
    const QString *a) {
  self->setAttributeExtraComment(*a);
}

//  void DomString::clearAttributeExtraComment()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomString26clearAttributeExtraCommentEv(DomString *self) {
  self->clearAttributeExtraComment();
}

//  bool DomString::hasAttributeId() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9DomString14hasAttributeIdEv(const DomString *self) {
  return self->hasAttributeId();
}

//  QString DomString::attributeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9DomString11attributeIdEv(const DomString *self) {
  return new QString(self->attributeId());
}

//  void DomString::setAttributeId(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomString14setAttributeIdERK7QString(
    DomString *self,
    const QString *a) {
  self->setAttributeId(*a);
}

//  void DomString::clearAttributeId()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomString16clearAttributeIdEv(DomString *self) {
  self->clearAttributeId();
}
