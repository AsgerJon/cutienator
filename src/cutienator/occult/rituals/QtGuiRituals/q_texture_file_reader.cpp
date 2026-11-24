//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtexturefilereader_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtexturefilereader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtexturefiledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  QTextureFileReader::QTextureFileReader(QIODevice *device, const QString
//      &fileName)
extern "C" Q_DECL_EXPORT
QTextureFileReader *ritual_ZN18QTextureFileReaderC1EP9QIODeviceRK7QString(
    QIODevice *device,
    const QString *fileName) {
  return new QTextureFileReader(device, *fileName);
}

//  QTextureFileReader::~QTextureFileReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextureFileReaderD1Ev(QTextureFileReader *self) {
  delete self;
}

//  bool QTextureFileReader::canRead()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QTextureFileReader7canReadEv(QTextureFileReader *self) {
  return self->canRead();
}

//  QTextureFileData QTextureFileReader::read()
extern "C" Q_DECL_EXPORT
QTextureFileData *ritual_ZN18QTextureFileReader4readEv(
    QTextureFileReader *self) {
  return new QTextureFileData(self->read());
}

//  QList<QByteArray> QTextureFileReader::supportedFileFormats()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN18QTextureFileReader20supportedFileFormatsEv() {
  return new QList<QByteArray>(QTextureFileReader::supportedFileFormats());
}

//  bool QTextureFileReader::init()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QTextureFileReader4initEv(QTextureFileReader *self) {
  return self->init();
}
