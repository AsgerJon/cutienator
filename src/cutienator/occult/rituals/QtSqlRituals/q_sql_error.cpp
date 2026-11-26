//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/qsqlerror.h, Qt 6.12.0. Changes made here are lost.
#include <QtSql/qsqlerror.h>
#include <QtCore/qstring.h>

//  QSqlError::QSqlError(const QString &driverText, const QString
//      &databaseText, ErrorType type, const QString &nativeErrorCode)
extern "C" Q_DECL_EXPORT
QSqlError *ritual_ZN9QSqlErrorC1ERK7QStringS2_NS_9ErrorTypeES2_(
    const QString *driverText,
    const QString *databaseText,
    QSqlError::ErrorType type,
    const QString *nativeErrorCode) {
  return new QSqlError(*driverText, *databaseText, type, *nativeErrorCode);
}

//  QSqlError::QSqlError(const QSqlError &other)
extern "C" Q_DECL_EXPORT
QSqlError *ritual_ZN9QSqlErrorC1ERKS_(const QSqlError *other) {
  return new QSqlError(*other);
}

//  QSqlError::QSqlError(QSqlError &&other)
extern "C" Q_DECL_EXPORT
QSqlError *ritual_ZN9QSqlErrorC1EOS_(QSqlError *other) {
  return new QSqlError(std::move(*other));
}

//  QSqlError &QSqlError::operator=(const QSqlError &other)
extern "C" Q_DECL_EXPORT
QSqlError *ritual_ZN9QSqlErroraSERKS_(
    QSqlError *self,
    const QSqlError *other) {
  return &(self->operator=(*other));
}

//  QSqlError &QSqlError::operator=(QSqlError &&other)
extern "C" Q_DECL_EXPORT
QSqlError *ritual_ZN9QSqlErroraSEOS_(QSqlError *self, QSqlError *other) {
  return &(self->operator=(std::move(*other)));
}

//  QSqlError::~QSqlError()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlErrorD1Ev(QSqlError *self) {
  delete self;
}

//  bool QSqlError::operator==(const QSqlError &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlErroreqERKS_(
    const QSqlError *self,
    const QSqlError *other) {
  return self->operator==(*other);
}

//  bool QSqlError::operator!=(const QSqlError &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlErrorneERKS_(
    const QSqlError *self,
    const QSqlError *other) {
  return self->operator!=(*other);
}

//  void QSqlError::swap(QSqlError &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlError4swapERS_(QSqlError *self, QSqlError *other) {
  self->swap(*other);
}

//  QString QSqlError::driverText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSqlError10driverTextEv(const QSqlError *self) {
  return new QString(self->driverText());
}

//  QString QSqlError::databaseText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSqlError12databaseTextEv(const QSqlError *self) {
  return new QString(self->databaseText());
}

//  ErrorType QSqlError::type() const
extern "C" Q_DECL_EXPORT
QSqlError::ErrorType ritual_ZNK9QSqlError4typeEv(const QSqlError *self) {
  return self->type();
}

//  QString QSqlError::nativeErrorCode() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSqlError15nativeErrorCodeEv(const QSqlError *self) {
  return new QString(self->nativeErrorCode());
}

//  QString QSqlError::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSqlError4textEv(const QSqlError *self) {
  return new QString(self->text());
}

//  bool QSqlError::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlError7isValidEv(const QSqlError *self) {
  return self->isValid();
}
