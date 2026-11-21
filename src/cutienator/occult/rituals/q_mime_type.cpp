//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmimetype.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmimetype.h>
#include <QtCore/qstring.h>

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
