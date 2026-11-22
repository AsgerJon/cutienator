//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstringconverter_base.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/QtCore>
#include <QtCore/qtestsupport_core.h>
#include <QtCore/qtmochelpers.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

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
