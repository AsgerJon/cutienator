//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvaspainter_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvaspainter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvasimage.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvaspainter.h>
#include <QtCanvasPainter/private/qcanvaspainter_p.h>
#include <QtGui/rhi/qrhi.h>
#include <QtCanvasPainter/qcanvasbrush.h>
#include <QtCanvasPainter/qcanvascustombrush.h>
#include <QtCanvasPainter/private/qcanvasimage_p.h>
#include <QtCanvasPainter/qcanvasboxshadow.h>
#include <QtCore/QLoggingCategory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/qcanvaspainter.cpp, line 2933, as _ZN19QCanvasImageTracker24removeTemporaryResourcesEv
inline void QCanvasImageTracker::removeTemporaryResources()
{
    m_doingResourcesRemoval = true;
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvaspainter.cpp, line 2939, as _ZN19QCanvasImageTracker15removeTextureIdEi
inline void QCanvasImageTracker::removeTextureId(int imageId)
{
    for (auto i = m_data.cbegin(), end = m_data.cend(); i != end; ++i) {
        if (i.value().id() == imageId) {
            m_cleanupTextures << i.value();
            break;
        }
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvaspainter.cpp, line 2989, as _ZN19QCanvasImageTracker17markTextureIdUsedEi
inline void QCanvasImageTracker::markTextureIdUsed(int imageId)
{
    if (imageId > 0 && !m_usedTextureIDs.contains(imageId))
        m_usedTextureIDs << imageId;
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvaspainter.cpp, line 2979, as _ZN19QCanvasImageTracker5clearEv
inline void QCanvasImageTracker::clear()
{
    m_data.clear();
    m_cleanupTextures.clear();
    m_usedTextureIDs.clear();
    m_dataAmount = 0;
    m_doingResourcesRemoval = false;
}
//  -----------------------------------------------------------------------

//  bool QCanvasImageTracker::contains(qint64 key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QCanvasImageTracker8containsEx(
    const QCanvasImageTracker *self,
    qint64 key) {
  return self->contains(key);
}

//  QCanvasImage QCanvasImageTracker::image(qint64 key) const
extern "C" Q_DECL_EXPORT
QCanvasImage *ritual_ZNK19QCanvasImageTracker5imageEx(
    const QCanvasImageTracker *self,
    qint64 key) {
  return new QCanvasImage(self->image(key));
}

//  int QCanvasImageTracker::textureId(qint64 key) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QCanvasImageTracker9textureIdEx(
    const QCanvasImageTracker *self,
    qint64 key) {
  return self->textureId(key);
}

//  void QCanvasImageTracker::insert(qint64 key, const QCanvasImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasImageTracker6insertExRK12QCanvasImage(
    QCanvasImageTracker *self,
    qint64 key,
    const QCanvasImage *image) {
  self->insert(key, *image);
}

//  qsizetype QCanvasImageTracker::dataAmount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK19QCanvasImageTracker10dataAmountEv(
    const QCanvasImageTracker *self) {
  return self->dataAmount();
}

//  qsizetype QCanvasImageTracker::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK19QCanvasImageTracker4sizeEv(
    const QCanvasImageTracker *self) {
  return self->size();
}

//  void QCanvasImageTracker::removeTemporaryResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasImageTracker24removeTemporaryResourcesEv(
    QCanvasImageTracker *self) {
  self->removeTemporaryResources();
}

//  void QCanvasImageTracker::removeTextureId(int imageId)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasImageTracker15removeTextureIdEi(
    QCanvasImageTracker *self,
    int imageId) {
  self->removeTextureId(imageId);
}

//  void QCanvasImageTracker::markTextureIdUsed(int imageId)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasImageTracker17markTextureIdUsedEi(
    QCanvasImageTracker *self,
    int imageId) {
  self->markTextureIdUsed(imageId);
}

//  void QCanvasImageTracker::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasImageTracker5clearEv(QCanvasImageTracker *self) {
  self->clear();
}

//  QCanvasImageTracker::~QCanvasImageTracker()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasImageTrackerD1Ev(QCanvasImageTracker *self) {
  delete self;
}
