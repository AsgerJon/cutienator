//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qformdatabuilder.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  added by hand, instances of templates of the class: 1. Kept as it is when
//  the generator runs again.
#include <QtNetwork/qtnetworkglobal.h>
#if (defined(Q_OS_WASM)) || (QT_CONFIG(http))
#if QT_CONFIG(http)
#include <QtNetwork/qformdatabuilder.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qbytearray.h>

//  QFormDataPartBuilder::QFormDataPartBuilder(QFormDataBuilderPrivate *qfdb,
//      qsizetype idx)
extern "C" Q_DECL_EXPORT
QFormDataPartBuilder *ritual_ZN20QFormDataPartBuilderC1EP23QFormDataBuilderPrivatex(
    QFormDataBuilderPrivate *qfdb,
    qsizetype idx) {
  return new QFormDataPartBuilder(qfdb, idx);
}

//  void QFormDataPartBuilder::swap(QFormDataPartBuilder &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFormDataPartBuilder4swapERS_(
    QFormDataPartBuilder *self,
    QFormDataPartBuilder *other) {
  self->swap(*other);
}

//  QFormDataPartBuilder::QFormDataPartBuilder()
extern "C" Q_DECL_EXPORT
QFormDataPartBuilder *ritual_ZN20QFormDataPartBuilderC1Ev() {
  return new QFormDataPartBuilder();
}

//  QFormDataPartBuilder QFormDataPartBuilder::setBody(QByteArrayView data,
//      QAnyStringView fileName, QAnyStringView mimeType)
extern "C" Q_DECL_EXPORT
QFormDataPartBuilder *ritual_ZN20QFormDataPartBuilder7setBodyE14QByteArrayView14QAnyStringViewS1_(
    QFormDataPartBuilder *self,
    const QByteArrayView *data,
    const QString *fileName,
    const QString *mimeType) {
  return new QFormDataPartBuilder(
      self->setBody(
          *data,
          QAnyStringView(*fileName),
          QAnyStringView(*mimeType)));
}

//  QFormDataPartBuilder QFormDataPartBuilder::setBodyDevice(QIODevice *body,
//      QAnyStringView fileName, QAnyStringView mimeType)
extern "C" Q_DECL_EXPORT
QFormDataPartBuilder *ritual_ZN20QFormDataPartBuilder13setBodyDeviceEP9QIODevice14QAnyStringViewS2_(
    QFormDataPartBuilder *self,
    QIODevice *body,
    const QString *fileName,
    const QString *mimeType) {
  return new QFormDataPartBuilder(
      self->setBodyDevice(
          body,
          QAnyStringView(*fileName),
          QAnyStringView(*mimeType)));
}

//  QFormDataPartBuilder QFormDataPartBuilder::setHeaders(const QHttpHeaders
//      &headers)
extern "C" Q_DECL_EXPORT
QFormDataPartBuilder *ritual_ZN20QFormDataPartBuilder10setHeadersERK12QHttpHeaders(
    QFormDataPartBuilder *self,
    const QHttpHeaders *headers) {
  return new QFormDataPartBuilder(self->setHeaders(*headers));
}

//  QFormDataPartBuilder QFormDataPartBuilder::setBodyHelper(const QByteArray
//      &data, QAnyStringView fileName, QAnyStringView mimeType)
extern "C" Q_DECL_EXPORT
QFormDataPartBuilder *ritual_ZN20QFormDataPartBuilder13setBodyHelperERK10QByteArray14QAnyStringViewS3_(
    QFormDataPartBuilder *self,
    const QByteArray *data,
    const QString *fileName,
    const QString *mimeType) {
  return new QFormDataPartBuilder(
      self->setBodyHelper(
          *data,
          QAnyStringView(*fileName),
          QAnyStringView(*mimeType)));
}

//  QFormDataPartBuilder::~QFormDataPartBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFormDataPartBuilderD1Ev(QFormDataPartBuilder *self) {
  delete self;
}

//  QFormDataPartBuilder QFormDataPartBuilder::setBody<void>(
//      const QByteArray &data, QAnyStringView fileName,
//      QAnyStringView mimeType)
extern "C" Q_DECL_EXPORT
QFormDataPartBuilder *ritual_ZN20QFormDataPartBuilder7setBodyIvEES_RK10QByteArray14QAnyStringViewS4_(
    QFormDataPartBuilder *self,
    const QByteArray *data,
    const QString *fileName,
    const QString *mimeType) {
  return new QFormDataPartBuilder(
      self->setBody<void>(
          *data,
          QAnyStringView(*fileName),
          QAnyStringView(*mimeType)));
}

#endif  // QT_CONFIG(http)
#endif  // (defined(Q_OS_WASM)) || (QT_CONFIG(http))
