//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgtexturereader_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgtexturereader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgtexturereader_p.h>
#include <QtGui/private/qtexturefilereader_p.h>
#include <QtQuick/private/qsgcompressedtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgtexturereader.cpp, line 11, as _ZN16QSGTextureReaderC1EP9QIODeviceRK7QString
inline QSGTextureReader::QSGTextureReader(QIODevice *device, const QString &fileName)
{
    m_reader = new QTextureFileReader(device, fileName);
}

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgtexturereader.cpp, line 16, as _ZN16QSGTextureReaderD1Ev
inline QSGTextureReader::~QSGTextureReader()
{
    delete m_reader;
}

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgtexturereader.cpp, line 21, as _ZN16QSGTextureReader4readEv
inline QQuickTextureFactory *QSGTextureReader::read()
{
    if (!m_reader)
        return nullptr;

    QTextureFileData texData = m_reader->read();
    if (!texData.isValid())
        return nullptr;

    return new QSGCompressedTextureFactory(texData);
}

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgtexturereader.cpp, line 33, as _ZN16QSGTextureReader9isTextureEv
inline bool QSGTextureReader::isTexture()
{
    return m_reader ? m_reader->canRead() : false;
}

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgtexturereader.cpp, line 38, as _ZN16QSGTextureReader20supportedFileFormatsEv
inline QList<QByteArray> QSGTextureReader::supportedFileFormats()
{
    return QTextureFileReader::supportedFileFormats();
}
//  -----------------------------------------------------------------------

//  QSGTextureReader::QSGTextureReader(QIODevice *device, const QString
//      &fileName)
extern "C" Q_DECL_EXPORT
QSGTextureReader *ritual_ZN16QSGTextureReaderC1EP9QIODeviceRK7QString(
    QIODevice *device,
    const QString *fileName) {
  return new QSGTextureReader(device, *fileName);
}

//  QSGTextureReader::~QSGTextureReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGTextureReaderD1Ev(QSGTextureReader *self) {
  delete self;
}

//  QQuickTextureFactory *QSGTextureReader::read()
extern "C" Q_DECL_EXPORT
QQuickTextureFactory *ritual_ZN16QSGTextureReader4readEv(
    QSGTextureReader *self) {
  return self->read();
}

//  bool QSGTextureReader::isTexture()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGTextureReader9isTextureEv(QSGTextureReader *self) {
  return self->isTexture();
}

//  QList<QByteArray> QSGTextureReader::supportedFileFormats()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN16QSGTextureReader20supportedFileFormatsEv() {
  return new QList<QByteArray>(QSGTextureReader::supportedFileFormats());
}
