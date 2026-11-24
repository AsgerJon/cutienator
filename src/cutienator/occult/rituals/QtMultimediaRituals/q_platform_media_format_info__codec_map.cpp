//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediaformatinfo_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediaformatinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>

//  QDebug operator<<(QDebug dbg, const CodecMap &m)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRKN24QPlatformMediaFormatInfo8CodecMapE(
    const QDebug *dbg,
    const QPlatformMediaFormatInfo::CodecMap *m) {
  return new QDebug(operator<<(*dbg, *m));
}

//  QPlatformMediaFormatInfo::CodecMap::~CodecMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlatformMediaFormatInfo8CodecMapD1Ev(
    QPlatformMediaFormatInfo::CodecMap *self) {
  delete self;
}
