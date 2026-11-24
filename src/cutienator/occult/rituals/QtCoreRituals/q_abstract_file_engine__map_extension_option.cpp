//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractfileengine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qabstractfileengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QAbstractFileEngine::MapExtensionOption::MapExtensionOption(qint64 off,
//      qint64 sz, QFile::MemoryMapFlags f)
extern "C" Q_DECL_EXPORT
QAbstractFileEngine::MapExtensionOption *ritual_ZN19QAbstractFileEngine18MapExtensionOptionC1Exx6QFlagsIN11QFileDevice13MemoryMapFlagEE(
    qint64 off,
    qint64 sz,
    int f) {
  return new QAbstractFileEngine::MapExtensionOption(
      off,
      sz,
      QFlags<QFileDevice::MemoryMapFlag>::fromInt(f));
}
