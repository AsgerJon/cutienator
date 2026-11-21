//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstringconverter.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qstringconverter.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>

//  QStringEncoder::QStringEncoder()
extern "C" Q_DECL_EXPORT
QStringEncoder *ritual_ZN14QStringEncoderC1Ev() {
  return new QStringEncoder();
}

//  QStringEncoder::QStringEncoder(Encoding encoding, Flags flags)
extern "C" Q_DECL_EXPORT
QStringEncoder *ritual_ZN14QStringEncoderC1EN16QStringConverter8EncodingE6QFlagsIN20QStringConverterBase4FlagEE(
    QStringConverter::Encoding encoding,
    int flags) {
  return new QStringEncoder(
      encoding,
      QFlags<QStringConverterBase::Flag>::fromInt(flags));
}

//  QStringEncoder::QStringEncoder(QAnyStringView name, Flags flags)
extern "C" Q_DECL_EXPORT
QStringEncoder *ritual_ZN14QStringEncoderC1E14QAnyStringView6QFlagsIN20QStringConverterBase4FlagEE(
    const QString *name,
    int flags) {
  return new QStringEncoder(
      QAnyStringView(*name),
      QFlags<QStringConverterBase::Flag>::fromInt(flags));
}

//  qsizetype QStringEncoder::requiredSpace(qsizetype inputLength) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QStringEncoder13requiredSpaceEx(
    const QStringEncoder *self,
    qsizetype inputLength) {
  return self->requiredSpace(inputLength);
}
