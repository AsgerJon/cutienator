//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtexturefiledata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtexturefiledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtGui/qimage.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qsize.h>
#include <QtCore/qdebug.h>
#include <QtCore/QMap>
#include <QtCore/QByteArray>

//  QTextureFileData::QTextureFileData(Mode mode)
extern "C" Q_DECL_EXPORT
QTextureFileData *ritual_ZN16QTextureFileDataC1ENS_4ModeE(
    QTextureFileData::Mode mode) {
  return new QTextureFileData(mode);
}

//  QTextureFileData::QTextureFileData(const QTextureFileData &other)
extern "C" Q_DECL_EXPORT
QTextureFileData *ritual_ZN16QTextureFileDataC1ERKS_(
    const QTextureFileData *other) {
  return new QTextureFileData(*other);
}

//  QTextureFileData::QTextureFileData(QTextureFileData &&a0)
extern "C" Q_DECL_EXPORT
QTextureFileData *ritual_ZN16QTextureFileDataC1EOS_(QTextureFileData *a0) {
  return new QTextureFileData(std::move(*a0));
}

//  QTextureFileData &QTextureFileData::operator=(const QTextureFileData
//      &other)
extern "C" Q_DECL_EXPORT
QTextureFileData *ritual_ZN16QTextureFileDataaSERKS_(
    QTextureFileData *self,
    const QTextureFileData *other) {
  return &(self->operator=(*other));
}

//  QTextureFileData &QTextureFileData::operator=(QTextureFileData &&other)
extern "C" Q_DECL_EXPORT
QTextureFileData *ritual_ZN16QTextureFileDataaSEOS_(
    QTextureFileData *self,
    QTextureFileData *other) {
  return &(self->operator=(std::move(*other)));
}

//  QTextureFileData::~QTextureFileData()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextureFileDataD1Ev(QTextureFileData *self) {
  delete self;
}

//  void QTextureFileData::swap(QTextureFileData &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextureFileData4swapERS_(
    QTextureFileData *self,
    QTextureFileData *other) {
  self->swap(*other);
}

//  bool QTextureFileData::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTextureFileData6isNullEv(const QTextureFileData *self) {
  return self->isNull();
}

//  bool QTextureFileData::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTextureFileData7isValidEv(const QTextureFileData *self) {
  return self->isValid();
}

//  void QTextureFileData::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextureFileData5clearEv(QTextureFileData *self) {
  self->clear();
}

//  QByteArray QTextureFileData::data() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QTextureFileData4dataEv(
    const QTextureFileData *self) {
  return new QByteArray(self->data());
}

//  void QTextureFileData::setData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextureFileData7setDataERK10QByteArray(
    QTextureFileData *self,
    const QByteArray *data) {
  self->setData(*data);
}

//  void QTextureFileData::setData(const QImage &image, int level, int face)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextureFileData7setDataERK6QImageii(
    QTextureFileData *self,
    const QImage *image,
    int level,
    int face) {
  self->setData(*image, level, face);
}

//  int QTextureFileData::dataOffset(int level, int face) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTextureFileData10dataOffsetEii(
    const QTextureFileData *self,
    int level,
    int face) {
  return self->dataOffset(level, face);
}

//  void QTextureFileData::setDataOffset(int offset, int level, int face)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextureFileData13setDataOffsetEiii(
    QTextureFileData *self,
    int offset,
    int level,
    int face) {
  self->setDataOffset(offset, level, face);
}

//  int QTextureFileData::dataLength(int level, int face) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTextureFileData10dataLengthEii(
    const QTextureFileData *self,
    int level,
    int face) {
  return self->dataLength(level, face);
}

//  void QTextureFileData::setDataLength(int length, int level, int face)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextureFileData13setDataLengthEiii(
    QTextureFileData *self,
    int length,
    int level,
    int face) {
  self->setDataLength(length, level, face);
}

//  QByteArrayView QTextureFileData::getDataView(int level, int face) const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK16QTextureFileData11getDataViewEii(
    const QTextureFileData *self,
    int level,
    int face) {
  return new QByteArrayView(self->getDataView(level, face));
}

//  int QTextureFileData::numLevels() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTextureFileData9numLevelsEv(const QTextureFileData *self) {
  return self->numLevels();
}

//  void QTextureFileData::setNumLevels(int num)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextureFileData12setNumLevelsEi(
    QTextureFileData *self,
    int num) {
  self->setNumLevels(num);
}

//  int QTextureFileData::numFaces() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTextureFileData8numFacesEv(const QTextureFileData *self) {
  return self->numFaces();
}

//  void QTextureFileData::setNumFaces(int num)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextureFileData11setNumFacesEi(
    QTextureFileData *self,
    int num) {
  self->setNumFaces(num);
}

//  QSize QTextureFileData::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QTextureFileData4sizeEv(const QTextureFileData *self) {
  return new QSize(self->size());
}

//  void QTextureFileData::setSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextureFileData7setSizeERK5QSize(
    QTextureFileData *self,
    const QSize *size) {
  self->setSize(*size);
}

//  quint32 QTextureFileData::glFormat() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK16QTextureFileData8glFormatEv(
    const QTextureFileData *self) {
  return self->glFormat();
}

//  void QTextureFileData::setGLFormat(quint32 format)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextureFileData11setGLFormatEj(
    QTextureFileData *self,
    quint32 format) {
  self->setGLFormat(format);
}

//  quint32 QTextureFileData::glInternalFormat() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK16QTextureFileData16glInternalFormatEv(
    const QTextureFileData *self) {
  return self->glInternalFormat();
}

//  void QTextureFileData::setGLInternalFormat(quint32 format)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextureFileData19setGLInternalFormatEj(
    QTextureFileData *self,
    quint32 format) {
  self->setGLInternalFormat(format);
}

//  quint32 QTextureFileData::glBaseInternalFormat() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK16QTextureFileData20glBaseInternalFormatEv(
    const QTextureFileData *self) {
  return self->glBaseInternalFormat();
}

//  void QTextureFileData::setGLBaseInternalFormat(quint32 format)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextureFileData23setGLBaseInternalFormatEj(
    QTextureFileData *self,
    quint32 format) {
  self->setGLBaseInternalFormat(format);
}

//  QByteArray QTextureFileData::logName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QTextureFileData7logNameEv(
    const QTextureFileData *self) {
  return new QByteArray(self->logName());
}

//  void QTextureFileData::setLogName(const QByteArray &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextureFileData10setLogNameERK10QByteArray(
    QTextureFileData *self,
    const QByteArray *name) {
  self->setLogName(*name);
}

//  QMap<QByteArray, QByteArray> QTextureFileData::keyValueMetadata() const
extern "C" Q_DECL_EXPORT
QMap<QByteArray, QByteArray> *ritual_ZNK16QTextureFileData16keyValueMetadataEv(
    const QTextureFileData *self) {
  return new QMap<QByteArray, QByteArray>(self->keyValueMetadata());
}

//  void QTextureFileData::setKeyValueMetadata(const QMap<QByteArray,
//      QByteArray> &keyValues)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextureFileData19setKeyValueMetadataERK4QMapI10QByteArrayS1_E(
    QTextureFileData *self,
    const QMap<QByteArray, QByteArray> *keyValues) {
  self->setKeyValueMetadata(*keyValues);
}

//  QDebug operator<<(QDebug dbg, const QTextureFileData &d)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK16QTextureFileData(
    const QDebug *dbg,
    const QTextureFileData *d) {
  return new QDebug(operator<<(*dbg, *d));
}

//  a QMap<QByteArray, QByteArray> a ritual of QTextureFileData gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTextureFileData__QMap_QByteArray_QByteArray(
    QMap<QByteArray, QByteArray> *self) {
  delete self;
}
