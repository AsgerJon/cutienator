//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  qdesigner_internal::PropertySheetTranslatableData::PropertySheetTranslata
//      bleData(bool translatable, const QString &disambiguation, const
//      QString &comment)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetTranslatableData *ritual_ZN18qdesigner_internal29PropertySheetTranslatableDataC1EbRK7QStringS3_(
    bool translatable,
    const QString *disambiguation,
    const QString *comment) {
  return new qdesigner_internal::PropertySheetTranslatableData(
      translatable,
      *disambiguation,
      *comment);
}

//  bool qdesigner_internal::PropertySheetTranslatableData::translatable()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal29PropertySheetTranslatableData12translatableEv(
    const qdesigner_internal::PropertySheetTranslatableData *self) {
  return self->translatable();
}

//  void
//      qdesigner_internal::PropertySheetTranslatableData::setTranslatable(bo
//      ol translatable)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal29PropertySheetTranslatableData15setTranslatableEb(
    qdesigner_internal::PropertySheetTranslatableData *self,
    bool translatable) {
  self->setTranslatable(translatable);
}

//  QString
//      qdesigner_internal::PropertySheetTranslatableData::disambiguation()
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal29PropertySheetTranslatableData14disambiguationEv(
    const qdesigner_internal::PropertySheetTranslatableData *self) {
  return new QString(self->disambiguation());
}

//  void qdesigner_internal::PropertySheetTranslatableData::setDisambiguation
//      (const QString &d)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal29PropertySheetTranslatableData17setDisambiguationERK7QString(
    qdesigner_internal::PropertySheetTranslatableData *self,
    const QString *d) {
  self->setDisambiguation(*d);
}

//  QString qdesigner_internal::PropertySheetTranslatableData::comment()
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal29PropertySheetTranslatableData7commentEv(
    const qdesigner_internal::PropertySheetTranslatableData *self) {
  return new QString(self->comment());
}

//  void qdesigner_internal::PropertySheetTranslatableData::setComment(const
//      QString &comment)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal29PropertySheetTranslatableData10setCommentERK7QString(
    qdesigner_internal::PropertySheetTranslatableData *self,
    const QString *comment) {
  self->setComment(*comment);
}

//  QString qdesigner_internal::PropertySheetTranslatableData::id() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal29PropertySheetTranslatableData2idEv(
    const qdesigner_internal::PropertySheetTranslatableData *self) {
  return new QString(self->id());
}

//  void qdesigner_internal::PropertySheetTranslatableData::setId(const
//      QString &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal29PropertySheetTranslatableData5setIdERK7QString(
    qdesigner_internal::PropertySheetTranslatableData *self,
    const QString *id) {
  self->setId(*id);
}

//  bool operator==(const PropertySheetTranslatableData &lhs, const
//      PropertySheetTranslatableData &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_29PropertySheetTranslatableDataES2_(
    const qdesigner_internal::PropertySheetTranslatableData *lhs,
    const qdesigner_internal::PropertySheetTranslatableData *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const PropertySheetTranslatableData &lhs, const
//      PropertySheetTranslatableData &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_29PropertySheetTranslatableDataES2_(
    const qdesigner_internal::PropertySheetTranslatableData *lhs,
    const qdesigner_internal::PropertySheetTranslatableData *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qdesigner_internal::PropertySheetTranslatableData::~PropertySheetTranslat
//      ableData()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal29PropertySheetTranslatableDataD1Ev(
    qdesigner_internal::PropertySheetTranslatableData *self) {
  delete self;
}
