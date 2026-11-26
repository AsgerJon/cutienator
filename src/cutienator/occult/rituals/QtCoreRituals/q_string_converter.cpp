//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstringconverter_base.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(Q_QDOC) && !defined(QT_BOOTSTRAPPED)
#include <QtCore/qstringconverter.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qlist.h>
#include <optional>
#include <QtCore/QStringConverter>
#include <QtCore/QAnyStringView>
#include <QtCore/QByteArrayView>

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

//  QStringConverter::QStringConverter(const Interface *i)
extern "C" Q_DECL_EXPORT
QStringConverter *ritual_ZN16QStringConverterC1EPKNS_9InterfaceE(
    const QStringConverter::Interface *i) {
  return new QStringConverter(i);
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

//  QStringConverter::QStringConverter(QStringConverter &&a0)
extern "C" Q_DECL_EXPORT
QStringConverter *ritual_ZN16QStringConverterC1EOS_(QStringConverter *a0) {
  return new QStringConverter(std::move(*a0));
}

//  QStringConverter &QStringConverter::operator=(QStringConverter &&a0)
extern "C" Q_DECL_EXPORT
QStringConverter *ritual_ZN16QStringConverteraSEOS_(
    QStringConverter *self,
    QStringConverter *a0) {
  return &(self->operator=(std::move(*a0)));
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

//  std::optional<Encoding> QStringConverter::encodingForName(QAnyStringView
//      name)
extern "C" Q_DECL_EXPORT
std::optional<QStringConverter::Encoding> *ritual_ZN16QStringConverter15encodingForNameE14QAnyStringView(
    const QString *name) {
  return new std::optional<QStringConverter::Encoding>(
      QStringConverter::encodingForName(
          QAnyStringView(*name)));
}

//  const char *QStringConverter::nameForEncoding(Encoding e)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN16QStringConverter15nameForEncodingENS_8EncodingE(
    QStringConverter::Encoding e) {
  return QStringConverter::nameForEncoding(e);
}

//  std::optional<Encoding> QStringConverter::encodingForData(QByteArrayView
//      data, char16_t expectedFirstCharacter)
extern "C" Q_DECL_EXPORT
std::optional<QStringConverter::Encoding> *ritual_ZN16QStringConverter15encodingForDataE14QByteArrayViewDs(
    const QByteArrayView *data,
    char16_t expectedFirstCharacter) {
  return new std::optional<QStringConverter::Encoding>(
      QStringConverter::encodingForData(
          *data,
          expectedFirstCharacter));
}

//  std::optional<Encoding> QStringConverter::encodingForHtml(QByteArrayView
//      data)
extern "C" Q_DECL_EXPORT
std::optional<QStringConverter::Encoding> *ritual_ZN16QStringConverter15encodingForHtmlE14QByteArrayView(
    const QByteArrayView *data) {
  return new std::optional<QStringConverter::Encoding>(
      QStringConverter::encodingForHtml(
          *data));
}

//  QStringList QStringConverter::availableCodecs()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN16QStringConverter15availableCodecsEv() {
  return new QList<QString>(QStringConverter::availableCodecs());
}

//  a std::optional<QStringConverter::Encoding> a ritual of QStringConverter
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStringConverter__std_optional_QStringConverter_Encoding(
    std::optional<QStringConverter::Encoding> *self) {
  delete self;
}

#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(Q_QDOC) && !defined(QT_BOOTSTRAPPED)
