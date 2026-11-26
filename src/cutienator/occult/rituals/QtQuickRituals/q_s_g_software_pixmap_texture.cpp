//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarepixmaptexture_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtGui/qpixmap.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtQuick/private/qsgcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaptexture.cpp, line 43, as _ZNK24QSGSoftwarePixmapTexture13comparisonKeyEv
inline qint64 QSGSoftwarePixmapTexture::comparisonKey() const
{
    return 0;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaptexture.cpp, line 28, as _ZNK24QSGSoftwarePixmapTexture11textureSizeEv
inline QSize QSGSoftwarePixmapTexture::textureSize() const
{
    return m_pixmap.size();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaptexture.cpp, line 33, as _ZNK24QSGSoftwarePixmapTexture15hasAlphaChannelEv
inline bool QSGSoftwarePixmapTexture::hasAlphaChannel() const
{
    return m_pixmap.hasAlphaChannel();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaptexture.cpp, line 38, as _ZNK24QSGSoftwarePixmapTexture10hasMipmapsEv
inline bool QSGSoftwarePixmapTexture::hasMipmaps() const
{
    return false;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QSGSoftwarePixmapTexture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QSGSoftwarePixmapTexture10metaObjectEv(
    const QSGSoftwarePixmapTexture *self) {
  return self->metaObject();
}

//  void *QSGSoftwarePixmapTexture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QSGSoftwarePixmapTexture11qt_metacastEPKc(
    QSGSoftwarePixmapTexture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGSoftwarePixmapTexture::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QSGSoftwarePixmapTexture11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGSoftwarePixmapTexture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  qint64 QSGSoftwarePixmapTexture::comparisonKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK24QSGSoftwarePixmapTexture13comparisonKeyEv(
    const QSGSoftwarePixmapTexture *self) {
  return self->comparisonKey();
}

//  QSize QSGSoftwarePixmapTexture::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK24QSGSoftwarePixmapTexture11textureSizeEv(
    const QSGSoftwarePixmapTexture *self) {
  return new QSize(self->textureSize());
}

//  bool QSGSoftwarePixmapTexture::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QSGSoftwarePixmapTexture15hasAlphaChannelEv(
    const QSGSoftwarePixmapTexture *self) {
  return self->hasAlphaChannel();
}

//  bool QSGSoftwarePixmapTexture::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QSGSoftwarePixmapTexture10hasMipmapsEv(
    const QSGSoftwarePixmapTexture *self) {
  return self->hasMipmaps();
}

//  const QPixmap &QSGSoftwarePixmapTexture::pixmap() const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK24QSGSoftwarePixmapTexture6pixmapEv(
    const QSGSoftwarePixmapTexture *self) {
  return new QPixmap(self->pixmap());
}

//  qint64 QSGSoftwarePixmapTexture::comparisonKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK24QSGSoftwarePixmapTexture13comparisonKeyEv(
    const QSGSoftwarePixmapTexture *self) {
  return self->QSGSoftwarePixmapTexture::comparisonKey();
}

//  QSize QSGSoftwarePixmapTexture::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK24QSGSoftwarePixmapTexture11textureSizeEv(
    const QSGSoftwarePixmapTexture *self) {
  return new QSize(self->QSGSoftwarePixmapTexture::textureSize());
}

//  bool QSGSoftwarePixmapTexture::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QSGSoftwarePixmapTexture15hasAlphaChannelEv(
    const QSGSoftwarePixmapTexture *self) {
  return self->QSGSoftwarePixmapTexture::hasAlphaChannel();
}

//  bool QSGSoftwarePixmapTexture::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QSGSoftwarePixmapTexture10hasMipmapsEv(
    const QSGSoftwarePixmapTexture *self) {
  return self->QSGSoftwarePixmapTexture::hasMipmaps();
}
