//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qspritesheet_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qspritesheet_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qabstractspritesheet.h>
#include <Qt3DExtras/private/qabstractspritesheet_p.h>
#include <Qt3DRender/qabstracttexture.h>
#include <Qt3DExtras/qspritesheet.h>
#include <Qt3DExtras/qspritesheetitem.h>
#include <Qt3DExtras/private/qspritesheet_p.h>
#include <Qt3DRender/qabstracttexture.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/defaults/qabstractspritesheet.cpp, line 16, as _ZN10Qt3DExtras27QAbstractSpriteSheetPrivateC2Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QAbstractSpriteSheetPrivate::QAbstractSpriteSheetPrivate()
    : QNodePrivate()
    , m_texture(nullptr)
    , m_currentIndex(-1)
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qspritesheet.cpp, line 22, as _ZNK10Qt3DExtras19QSpriteSheetPrivate8maxIndexEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline int QSpriteSheetPrivate::maxIndex() const
{
    return m_sprites.size() - 1;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qspritesheet.cpp, line 27, as _ZN10Qt3DExtras19QSpriteSheetPrivate11updateSizesEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void QSpriteSheetPrivate::updateSizes()
{
    Q_Q(QSpriteSheet);
    if (m_texture)
        m_textureSize = QSize(m_texture->width(), m_texture->height());
    else
        m_textureSize = QSize();

    if (m_textureSize.isEmpty() || m_sprites.isEmpty()) {
        if (m_currentIndex != -1) {
            m_currentIndex = -1;
            emit q->currentIndexChanged(m_currentIndex);
        }
        m_textureTransform.setToIdentity();
        emit q->textureTransformChanged(m_textureTransform);
        return;
    }

    if (m_currentIndex < 0 || m_currentIndex >= m_sprites.size()) {
        m_currentIndex = 0;
        emit q->currentIndexChanged(m_currentIndex);
    }
    updateTransform();
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qspritesheet.cpp, line 52, as _ZN10Qt3DExtras19QSpriteSheetPrivate15updateTransformEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void QSpriteSheetPrivate::updateTransform()
{
    Q_Q(QSpriteSheet);
    if (m_currentIndex < 0 || m_currentIndex >= m_sprites.size())
        return;

    const QSpriteSheetItem *r = m_sprites.at(m_currentIndex);
    const float xScale = static_cast<float>(r->width()) / static_cast<float>(m_textureSize.width());
    const float yScale = static_cast<float>(r->height()) / static_cast<float>(m_textureSize.height());

    const float xTranslate = static_cast<float>(r->x()) / static_cast<float>(m_textureSize.width());
    const float yTranslate = static_cast<float>(r->y()) / static_cast<float>(m_textureSize.height());

    m_textureTransform.setToIdentity();
    m_textureTransform(0, 0) = xScale;
    m_textureTransform(1, 1) = yScale;
    m_textureTransform(0, 2) = xTranslate;
    m_textureTransform(1, 2) = yTranslate;
    emit q->textureTransformChanged(m_textureTransform);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qabstractspritesheet.cpp, line 23, as _ZN10Qt3DExtras27QAbstractSpriteSheetPrivate4initEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void QAbstractSpriteSheetPrivate::init()
{
    m_textureTransform.setToIdentity();
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  int Qt3DExtras::QSpriteSheetPrivate::maxIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras19QSpriteSheetPrivate8maxIndexEv(
    const Qt3DExtras::QSpriteSheetPrivate *self) {
  return self->maxIndex();
}

//  void Qt3DExtras::QSpriteSheetPrivate::updateSizes()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QSpriteSheetPrivate11updateSizesEv(
    Qt3DExtras::QSpriteSheetPrivate *self) {
  self->updateSizes();
}

//  void Qt3DExtras::QSpriteSheetPrivate::updateTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QSpriteSheetPrivate15updateTransformEv(
    Qt3DExtras::QSpriteSheetPrivate *self) {
  self->updateTransform();
}

//  QSpriteSheet *Qt3DExtras::QSpriteSheetPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSpriteSheet *ritual_ZN10Qt3DExtras19QSpriteSheetPrivate6q_funcEv(
    Qt3DExtras::QSpriteSheetPrivate *self) {
  return self->q_func();
}

//  const QSpriteSheet *Qt3DExtras::QSpriteSheetPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QSpriteSheet *ritual_ZNK10Qt3DExtras19QSpriteSheetPrivate6q_funcEv(
    const Qt3DExtras::QSpriteSheetPrivate *self) {
  return self->q_func();
}

//  int Qt3DExtras::QSpriteSheetPrivate::maxIndex() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10Qt3DExtras19QSpriteSheetPrivate8maxIndexEv(
    const Qt3DExtras::QSpriteSheetPrivate *self) {
  return self->Qt3DExtras::QSpriteSheetPrivate::maxIndex();
}

//  void Qt3DExtras::QSpriteSheetPrivate::updateSizes()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DExtras19QSpriteSheetPrivate11updateSizesEv(
    Qt3DExtras::QSpriteSheetPrivate *self) {
  self->Qt3DExtras::QSpriteSheetPrivate::updateSizes();
}

//  void Qt3DExtras::QSpriteSheetPrivate::updateTransform()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DExtras19QSpriteSheetPrivate15updateTransformEv(
    Qt3DExtras::QSpriteSheetPrivate *self) {
  self->Qt3DExtras::QSpriteSheetPrivate::updateTransform();
}
