//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qsslerror.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if !defined(QT_NO_SSL)
#include <QtNetwork/qsslerror.h>
#include <QtNetwork/qsslcertificate.h>
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QSslError::QSslError()
extern "C" Q_DECL_EXPORT
QSslError *ritual_ZN9QSslErrorC1Ev() {
  return new QSslError();
}

//  QSslError::QSslError(SslError error)
extern "C" Q_DECL_EXPORT
QSslError *ritual_ZN9QSslErrorC1ENS_8SslErrorE(QSslError::SslError error) {
  return new QSslError(error);
}

//  QSslError::QSslError(SslError error, const QSslCertificate &certificate)
extern "C" Q_DECL_EXPORT
QSslError *ritual_ZN9QSslErrorC1ENS_8SslErrorERK15QSslCertificate(
    QSslError::SslError error,
    const QSslCertificate *certificate) {
  return new QSslError(error, *certificate);
}

//  QSslError::QSslError(const QSslError &other)
extern "C" Q_DECL_EXPORT
QSslError *ritual_ZN9QSslErrorC1ERKS_(const QSslError *other) {
  return new QSslError(*other);
}

//  void QSslError::swap(QSslError &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSslError4swapERS_(QSslError *self, QSslError *other) {
  self->swap(*other);
}

//  QSslError::~QSslError()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSslErrorD1Ev(QSslError *self) {
  delete self;
}

//  QSslError &QSslError::operator=(QSslError &&other)
extern "C" Q_DECL_EXPORT
QSslError *ritual_ZN9QSslErroraSEOS_(QSslError *self, QSslError *other) {
  return &(self->operator=(std::move(*other)));
}

//  QSslError &QSslError::operator=(const QSslError &other)
extern "C" Q_DECL_EXPORT
QSslError *ritual_ZN9QSslErroraSERKS_(
    QSslError *self,
    const QSslError *other) {
  return &(self->operator=(*other));
}

//  bool QSslError::operator==(const QSslError &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSslErroreqERKS_(
    const QSslError *self,
    const QSslError *other) {
  return self->operator==(*other);
}

//  bool QSslError::operator!=(const QSslError &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSslErrorneERKS_(
    const QSslError *self,
    const QSslError *other) {
  return self->operator!=(*other);
}

//  SslError QSslError::error() const
extern "C" Q_DECL_EXPORT
QSslError::SslError ritual_ZNK9QSslError5errorEv(const QSslError *self) {
  return self->error();
}

//  QString QSslError::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSslError11errorStringEv(const QSslError *self) {
  return new QString(self->errorString());
}

//  QSslCertificate QSslError::certificate() const
extern "C" Q_DECL_EXPORT
QSslCertificate *ritual_ZNK9QSslError11certificateEv(const QSslError *self) {
  return new QSslCertificate(self->certificate());
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, SslError error)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugN9QSslError8SslErrorE(
    const QDebug *debug,
    QSslError::SslError error) {
  return new QDebug(operator<<(*debug, error));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QList<QSslError>::QList()
extern "C" Q_DECL_EXPORT
QList<QSslError> *ritual_list_make_QSslError() {
  return new QList<QSslError>();
}

//  void QList<QSslError>::append(const QSslError &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSslError(
    QList<QSslError> *self,
    const QSslError *element) {
  self->append(*element);
}

//  qsizetype QList<QSslError>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSslError(const QList<QSslError> *self) {
  return self->size();
}

//  const QSslError &QList<QSslError>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QSslError *ritual_list_at_QSslError(
    const QList<QSslError> *self,
    long long index) {
  return new QSslError(self->at(index));
}

//  QList<QSslError>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSslError(QList<QSslError> *self) {
  delete self;
}

#endif  // !defined(QT_NO_SSL)
