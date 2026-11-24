//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcborstreamwriter.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(cborstreamwriter)
#include <QtCore/qcborstreamwriter.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetatype.h>

//  QCborStreamWriter::QCborStreamWriter(QIODevice *device)
extern "C" Q_DECL_EXPORT
QCborStreamWriter *ritual_ZN17QCborStreamWriterC1EP9QIODevice(
    QIODevice *device) {
  return new QCborStreamWriter(device);
}

//  QCborStreamWriter::QCborStreamWriter(QByteArray *data)
extern "C" Q_DECL_EXPORT
QCborStreamWriter *ritual_ZN17QCborStreamWriterC1EP10QByteArray(
    QByteArray *data) {
  return new QCborStreamWriter(data);
}

//  QCborStreamWriter::~QCborStreamWriter()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriterD1Ev(QCborStreamWriter *self) {
  delete self;
}

//  void QCborStreamWriter::setDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter9setDeviceEP9QIODevice(
    QCborStreamWriter *self,
    QIODevice *device) {
  self->setDevice(device);
}

//  QIODevice *QCborStreamWriter::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK17QCborStreamWriter6deviceEv(
    const QCborStreamWriter *self) {
  return self->device();
}

//  void QCborStreamWriter::append(quint64 u)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter6appendEy(
    QCborStreamWriter *self,
    quint64 u) {
  self->append(u);
}

//  void QCborStreamWriter::append(qint64 i)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter6appendEx(
    QCborStreamWriter *self,
    qint64 i) {
  self->append(i);
}

//  void QCborStreamWriter::append(QCborNegativeInteger n)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter6appendE20QCborNegativeInteger(
    QCborStreamWriter *self,
    QCborNegativeInteger n) {
  self->append(n);
}

//  void QCborStreamWriter::append(QByteArrayView ba)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter6appendE14QByteArrayView(
    QCborStreamWriter *self,
    const QByteArrayView *ba) {
  self->append(*ba);
}

//  void QCborStreamWriter::append(QLatin1StringView str)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter6appendE13QLatin1String(
    QCborStreamWriter *self,
    const QLatin1String *str) {
  self->append(*str);
}

//  void QCborStreamWriter::append(QStringView str)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter6appendE11QStringView(
    QCborStreamWriter *self,
    const QString *str) {
  self->append(QStringView(*str));
}

//  void QCborStreamWriter::append(QCborTag tag)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter6appendE8QCborTag(
    QCborStreamWriter *self,
    QCborTag tag) {
  self->append(tag);
}

//  void QCborStreamWriter::append(QCborKnownTags tag)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter6appendE14QCborKnownTags(
    QCborStreamWriter *self,
    QCborKnownTags tag) {
  self->append(tag);
}

//  void QCborStreamWriter::append(QCborSimpleType st)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter6appendE15QCborSimpleType(
    QCborStreamWriter *self,
    QCborSimpleType st) {
  self->append(st);
}

#if !defined(QT_BOOTSTRAPPED)
//  void QCborStreamWriter::append(qfloat16 f)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter6appendE8qfloat16(
    QCborStreamWriter *self,
    const qfloat16 *f) {
  self->append(*f);
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  void QCborStreamWriter::append(float f)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter6appendEf(
    QCborStreamWriter *self,
    float f) {
  self->append(f);
}

//  void QCborStreamWriter::append(double d)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter6appendEd(
    QCborStreamWriter *self,
    double d) {
  self->append(d);
}

//  void QCborStreamWriter::appendByteString(const char *data, qsizetype len)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter16appendByteStringEPKcx(
    QCborStreamWriter *self,
    const char *data,
    qsizetype len) {
  self->appendByteString(data, len);
}

//  void QCborStreamWriter::appendTextString(const char *utf8, qsizetype len)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter16appendTextStringEPKcx(
    QCborStreamWriter *self,
    const char *utf8,
    qsizetype len) {
  self->appendTextString(utf8, len);
}

//  void QCborStreamWriter::append(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter6appendEb(QCborStreamWriter *self, bool b) {
  self->append(b);
}

//  void QCborStreamWriter::appendNull()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter10appendNullEv(QCborStreamWriter *self) {
  self->appendNull();
}

//  void QCborStreamWriter::appendUndefined()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter15appendUndefinedEv(
    QCborStreamWriter *self) {
  self->appendUndefined();
}

#if !defined(Q_QDOC)
//  void QCborStreamWriter::append(int i)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter6appendEi(QCborStreamWriter *self, int i) {
  self->append(i);
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  void QCborStreamWriter::append(uint u)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter6appendEj(QCborStreamWriter *self, uint u) {
  self->append(u);
}
#endif  // !defined(Q_QDOC)

#if !defined(QT_NO_CAST_FROM_ASCII)
//  void QCborStreamWriter::append(const char *str, qsizetype size)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter6appendEPKcx(
    QCborStreamWriter *self,
    const char *str,
    qsizetype size) {
  self->append(str, size);
}
#endif  // !defined(QT_NO_CAST_FROM_ASCII)

//  void QCborStreamWriter::startArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter10startArrayEv(QCborStreamWriter *self) {
  self->startArray();
}

//  void QCborStreamWriter::startArray(quint64 count)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter10startArrayEy(
    QCborStreamWriter *self,
    quint64 count) {
  self->startArray(count);
}

//  bool QCborStreamWriter::endArray()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QCborStreamWriter8endArrayEv(QCborStreamWriter *self) {
  return self->endArray();
}

//  void QCborStreamWriter::startMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter8startMapEv(QCborStreamWriter *self) {
  self->startMap();
}

//  void QCborStreamWriter::startMap(quint64 count)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamWriter8startMapEy(
    QCborStreamWriter *self,
    quint64 count) {
  self->startMap(count);
}

//  bool QCborStreamWriter::endMap()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QCborStreamWriter6endMapEv(QCborStreamWriter *self) {
  return self->endMap();
}

#endif  // QT_CONFIG(cborstreamwriter)
