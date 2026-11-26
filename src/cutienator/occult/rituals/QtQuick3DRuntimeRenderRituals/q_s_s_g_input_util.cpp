//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderloadedtexture_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderloadedtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/QSharedPointer>
#include <QtCore/QIODevice>
#include <QtCore/QString>

//  QSharedPointer<QIODevice> QSSGInputUtil::getStreamForFile(const QString
//      &inPath, bool inQuiet, QString *outPath)
extern "C" Q_DECL_EXPORT
QSharedPointer<QIODevice> *ritual_ZN13QSSGInputUtil16getStreamForFileERK7QStringbPS0_(
    const QString *inPath,
    bool inQuiet,
    QString *outPath) {
  return new QSharedPointer<QIODevice>(
      QSSGInputUtil::getStreamForFile(
          *inPath,
          inQuiet,
          outPath));
}

//  QSharedPointer<QIODevice> QSSGInputUtil::getStreamForTextureFile(const
//      QString &inPath, bool inQuiet, QString *outPath, FileType
//      *outFileType)
extern "C" Q_DECL_EXPORT
QSharedPointer<QIODevice> *ritual_ZN13QSSGInputUtil23getStreamForTextureFileERK7QStringbPS0_PNS_8FileTypeE(
    const QString *inPath,
    bool inQuiet,
    QString *outPath,
    QSSGInputUtil::FileType *outFileType) {
  return new QSharedPointer<QIODevice>(
      QSSGInputUtil::getStreamForTextureFile(
          *inPath,
          inQuiet,
          outPath,
          outFileType));
}

//  QSSGInputUtil::~QSSGInputUtil()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGInputUtilD1Ev(QSSGInputUtil *self) {
  delete self;
}

//  a QSharedPointer<QIODevice> a ritual of QSSGInputUtil gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGInputUtil__QSharedPointer_QIODevice(
    QSharedPointer<QIODevice> *self) {
  delete self;
}
