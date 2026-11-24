//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qxmlstream_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qxmlstream_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QXmlStreamReaderPrivate::BufferAndEncoding::BufferAndEncoding()
extern "C" Q_DECL_EXPORT
QXmlStreamReaderPrivate::BufferAndEncoding *ritual_ZN23QXmlStreamReaderPrivate17BufferAndEncodingC1Ev() {
  return new QXmlStreamReaderPrivate::BufferAndEncoding();
}

//  QXmlStreamReaderPrivate::BufferAndEncoding::~BufferAndEncoding()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate17BufferAndEncodingD1Ev(
    QXmlStreamReaderPrivate::BufferAndEncoding *self) {
  delete self;
}

#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)
