//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmimetype.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
#include <QtCore/qmimetype.h>
#if QT_CONFIG(mimetype)
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimetype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QMimeType::QMimeType()
extern "C" Q_DECL_EXPORT
QMimeType *ritual_ZN9QMimeTypeC1Ev() {
  return new QMimeType();
}

//  QMimeType::QMimeType(const QMimeType &other)
extern "C" Q_DECL_EXPORT
QMimeType *ritual_ZN9QMimeTypeC1ERKS_(const QMimeType *other) {
  return new QMimeType(*other);
}

//  QMimeType &QMimeType::operator=(const QMimeType &other)
extern "C" Q_DECL_EXPORT
QMimeType *ritual_ZN9QMimeTypeaSERKS_(
    QMimeType *self,
    const QMimeType *other) {
  return &(self->operator=(*other));
}

//  QMimeType &QMimeType::operator=(QMimeType &&other)
extern "C" Q_DECL_EXPORT
QMimeType *ritual_ZN9QMimeTypeaSEOS_(QMimeType *self, QMimeType *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QMimeType::swap(QMimeType &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeType4swapERS_(QMimeType *self, QMimeType *other) {
  self->swap(*other);
}

//  QMimeType::QMimeType(const QMimeTypePrivate &dd)
extern "C" Q_DECL_EXPORT
QMimeType *ritual_ZN9QMimeTypeC1ERK16QMimeTypePrivate(
    const QMimeTypePrivate *dd) {
  return new QMimeType(*dd);
}

//  QMimeType::~QMimeType()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeTypeD1Ev(QMimeType *self) {
  delete self;
}

//  bool QMimeType::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMimeType7isValidEv(const QMimeType *self) {
  return self->isValid();
}

//  bool QMimeType::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMimeType9isDefaultEv(const QMimeType *self) {
  return self->isDefault();
}

//  QString QMimeType::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QMimeType4nameEv(const QMimeType *self) {
  return new QString(self->name());
}

//  QString QMimeType::comment() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QMimeType7commentEv(const QMimeType *self) {
  return new QString(self->comment());
}

//  QString QMimeType::genericIconName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QMimeType15genericIconNameEv(const QMimeType *self) {
  return new QString(self->genericIconName());
}

//  QString QMimeType::iconName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QMimeType8iconNameEv(const QMimeType *self) {
  return new QString(self->iconName());
}

//  QStringList QMimeType::globPatterns() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9QMimeType12globPatternsEv(const QMimeType *self) {
  return new QList<QString>(self->globPatterns());
}

//  QStringList QMimeType::parentMimeTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9QMimeType15parentMimeTypesEv(
    const QMimeType *self) {
  return new QList<QString>(self->parentMimeTypes());
}

//  QStringList QMimeType::allAncestors() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9QMimeType12allAncestorsEv(const QMimeType *self) {
  return new QList<QString>(self->allAncestors());
}

//  QStringList QMimeType::aliases() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9QMimeType7aliasesEv(const QMimeType *self) {
  return new QList<QString>(self->aliases());
}

//  QStringList QMimeType::suffixes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9QMimeType8suffixesEv(const QMimeType *self) {
  return new QList<QString>(self->suffixes());
}

//  QString QMimeType::preferredSuffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QMimeType15preferredSuffixEv(const QMimeType *self) {
  return new QString(self->preferredSuffix());
}

//  bool QMimeType::inherits(const QString &mimeTypeName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMimeType8inheritsERK7QString(
    const QMimeType *self,
    const QString *mimeTypeName) {
  return self->inherits(*mimeTypeName);
}

//  QString QMimeType::filterString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QMimeType12filterStringEv(const QMimeType *self) {
  return new QString(self->filterString());
}

//  bool operator==(const QMimeType &lhs, const QMimeType &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK9QMimeTypeS1_(const QMimeType *lhs, const QMimeType *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QMimeType &lhs, const QMimeType &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK9QMimeTypeS1_(const QMimeType *lhs, const QMimeType *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QList<QMimeType>::QList()
extern "C" Q_DECL_EXPORT
QList<QMimeType> *ritual_list_make_QMimeType() {
  return new QList<QMimeType>();
}

//  void QList<QMimeType>::append(const QMimeType &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QMimeType(
    QList<QMimeType> *self,
    const QMimeType *element) {
  self->append(*element);
}

//  qsizetype QList<QMimeType>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QMimeType(const QList<QMimeType> *self) {
  return self->size();
}

//  const QMimeType &QList<QMimeType>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QMimeType *ritual_list_at_QMimeType(
    const QList<QMimeType> *self,
    long long index) {
  return new QMimeType(self->at(index));
}

//  QList<QMimeType>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QMimeType(QList<QMimeType> *self) {
  delete self;
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
