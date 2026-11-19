//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qbuffer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qbuffer.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  const QMetaObject *QBuffer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QBuffer10metaObjectEv(const QBuffer *self) {
  return self->metaObject();
}

//  QString QBuffer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QBuffer2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QBuffer::tr(s, c, n));
}

//  QBuffer::QBuffer(QObject *parent)
extern "C" Q_DECL_EXPORT
QBuffer *ritual_ZN7QBufferC1EP7QObject(QObject *parent) {
  return new QBuffer(parent);
}

//  QBuffer::QBuffer(QByteArray *buf, QObject *parent)
extern "C" Q_DECL_EXPORT
QBuffer *ritual_ZN7QBufferC1EP10QByteArrayP7QObject(
    QByteArray *buf,
    QObject *parent) {
  return new QBuffer(buf, parent);
}

//  QBuffer::~QBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBufferD1Ev(QBuffer *self) {
  delete self;
}

//  const QByteArray &QBuffer::buffer() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK7QBuffer6bufferEv(const QBuffer *self) {
  return new QByteArray(self->buffer());
}

//  void QBuffer::setBuffer(QByteArray *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBuffer9setBufferEP10QByteArray(
    QBuffer *self,
    QByteArray *a) {
  self->setBuffer(a);
}

//  void QBuffer::setData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBuffer7setDataERK10QByteArray(
    QBuffer *self,
    const QByteArray *data) {
  self->setData(*data);
}

//  void QBuffer::setData(const char *data, qsizetype len)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBuffer7setDataEPKcx(
    QBuffer *self,
    const char *data,
    qsizetype len) {
  self->setData(data, len);
}

//  const QByteArray &QBuffer::data() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK7QBuffer4dataEv(const QBuffer *self) {
  return new QByteArray(self->data());
}

//  bool QBuffer::open(OpenMode openMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QBuffer4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBuffer *self,
    int openMode) {
  return self->open(QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QBuffer::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBuffer5closeEv(QBuffer *self) {
  self->close();
}

//  qint64 QBuffer::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK7QBuffer4sizeEv(const QBuffer *self) {
  return self->size();
}

//  qint64 QBuffer::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK7QBuffer3posEv(const QBuffer *self) {
  return self->pos();
}

//  bool QBuffer::seek(qint64 off)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QBuffer4seekEx(QBuffer *self, qint64 off) {
  return self->seek(off);
}

//  bool QBuffer::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QBuffer5atEndEv(const QBuffer *self) {
  return self->atEnd();
}

//  bool QBuffer::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QBuffer11canReadLineEv(const QBuffer *self) {
  return self->canReadLine();
}
