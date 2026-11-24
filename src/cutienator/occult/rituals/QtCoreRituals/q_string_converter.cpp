//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstringconverter_base.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(Q_QDOC) && !defined(QT_BOOTSTRAPPED)
#include <QtCore/qstringconverter.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QStringConverter::QStringConverter()
extern "C" Q_DECL_EXPORT
QStringConverter *ritual_ZN16QStringConverterC1Ev() {
  return new QStringConverter();
}

//  QStringConverter::QStringConverter(Encoding encoding, Flags f)
extern "C" Q_DECL_EXPORT
QStringConverter *ritual_ZN16QStringConverterC1ENS_8EncodingE6QFlagsIN20QStringConverterBase4FlagEE(
    QStringConverter::Encoding encoding,
    int f) {
  return new QStringConverter(
      encoding,
      QFlags<QStringConverterBase::Flag>::fromInt(f));
}

//  QStringConverter::QStringConverter(QAnyStringView name, Flags f)
extern "C" Q_DECL_EXPORT
QStringConverter *ritual_ZN16QStringConverterC1E14QAnyStringView6QFlagsIN20QStringConverterBase4FlagEE(
    const QString *name,
    int f) {
  return new QStringConverter(
      QAnyStringView(*name),
      QFlags<QStringConverterBase::Flag>::fromInt(f));
}

//  QStringConverter::~QStringConverter()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QStringConverterD1Ev(QStringConverter *self) {
  delete self;
}

//  bool QStringConverter::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QStringConverter7isValidEv(const QStringConverter *self) {
  return self->isValid();
}

//  void QStringConverter::resetState()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QStringConverter10resetStateEv(QStringConverter *self) {
  self->resetState();
}

//  bool QStringConverter::hasError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QStringConverter8hasErrorEv(const QStringConverter *self) {
  return self->hasError();
}

//  const char *QStringConverter::name() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK16QStringConverter4nameEv(
    const QStringConverter *self) {
  return self->name();
}

//  const char *QStringConverter::nameForEncoding(Encoding e)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN16QStringConverter15nameForEncodingENS_8EncodingE(
    QStringConverter::Encoding e) {
  return QStringConverter::nameForEncoding(e);
}

//  QStringList QStringConverter::availableCodecs()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN16QStringConverter15availableCodecsEv() {
  return new QList<QString>(QStringConverter::availableCodecs());
}

#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(Q_QDOC) && !defined(QT_BOOTSTRAPPED)
