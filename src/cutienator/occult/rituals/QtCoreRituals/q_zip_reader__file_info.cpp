//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qzipreader_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qzipreader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QZipReader::FileInfo::FileInfo()
extern "C" Q_DECL_EXPORT
QZipReader::FileInfo *ritual_ZN10QZipReader8FileInfoC1Ev() {
  return new QZipReader::FileInfo();
}

//  bool QZipReader::FileInfo::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QZipReader8FileInfo7isValidEv(
    const QZipReader::FileInfo *self) {
  return self->isValid();
}

//  QZipReader::FileInfo::~FileInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QZipReader8FileInfoD1Ev(QZipReader::FileInfo *self) {
  delete self;
}
