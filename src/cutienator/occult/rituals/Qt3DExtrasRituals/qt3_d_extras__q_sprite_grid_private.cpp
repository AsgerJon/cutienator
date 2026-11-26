//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qspritegrid_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qspritegrid_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qabstractspritesheet.h>
#include <Qt3DExtras/private/qabstractspritesheet_p.h>
#include <Qt3DRender/qabstracttexture.h>
#include <Qt3DExtras/qspritegrid.h>
#include <Qt3DExtras/private/qspritegrid_p.h>
#include <Qt3DRender/qabstracttexture.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from ../qt3d/src/extras/defaults/qspritegrid.cpp, line 23, as _ZNK10Qt3DExtras18QSpriteGridPrivate8maxIndexEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline int QSpriteGridPrivate::maxIndex() const
{
    return m_numColumns * m_numRows - 1;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qspritegrid.cpp, line 28, as _ZN10Qt3DExtras18QSpriteGridPrivate11updateSizesEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void QSpriteGridPrivate::updateSizes()
{
    Q_Q(QSpriteGrid);
    if (m_texture && m_numColumns && m_numRows) {
        m_textureSize = QSize(m_texture->width(), m_texture->height());
        m_cellSize = QSizeF((float) m_texture->width() / m_numColumns, (float) m_texture->height() / m_numRows);
    } else {
        m_textureSize = QSize();
        m_cellSize = QSizeF();
    }

    if (m_cellSize.isEmpty() || m_numColumns == 0 || m_numRows == 0) {
        if (m_currentIndex != -1) {
            m_currentIndex = -1;
            emit q->currentIndexChanged(m_currentIndex);
        }
        m_textureTransform.setToIdentity();
        emit q->textureTransformChanged(m_textureTransform);
        return;
    }

    if (m_currentIndex == -1) {
        m_currentIndex = 0;
        emit q->currentIndexChanged(m_currentIndex);
    }
    updateTransform();
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qspritegrid.cpp, line 56, as _ZN10Qt3DExtras18QSpriteGridPrivate15updateTransformEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void QSpriteGridPrivate::updateTransform()
{
    Q_Q(QSpriteGrid);
    const float xScale = (float) m_cellSize.width() / (float) m_textureSize.width();
    const float yScale = (float) m_cellSize.height() / (float) m_textureSize.height();

    const int currentRow = m_currentIndex / m_numColumns;
    const int currentColumn = m_currentIndex % m_numColumns;
    const float xTranslate = currentColumn * xScale;
    const float yTranslate = currentRow * yScale;

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

//  from ../qt3d/src/extras/defaults/qspritegrid.cpp, line 16, as _ZN10Qt3DExtras18QSpriteGridPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QSpriteGridPrivate::QSpriteGridPrivate()
    : QAbstractSpriteSheetPrivate()
    , m_numColumns(1)
    , m_numRows(1)
{
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  Qt3DExtras::QSpriteGridPrivate::QSpriteGridPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSpriteGridPrivate *ritual_ZN10Qt3DExtras18QSpriteGridPrivateC1Ev() {
  return new Qt3DExtras::QSpriteGridPrivate();
}

//  int Qt3DExtras::QSpriteGridPrivate::maxIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras18QSpriteGridPrivate8maxIndexEv(
    const Qt3DExtras::QSpriteGridPrivate *self) {
  return self->maxIndex();
}

//  void Qt3DExtras::QSpriteGridPrivate::updateSizes()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras18QSpriteGridPrivate11updateSizesEv(
    Qt3DExtras::QSpriteGridPrivate *self) {
  self->updateSizes();
}

//  void Qt3DExtras::QSpriteGridPrivate::updateTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras18QSpriteGridPrivate15updateTransformEv(
    Qt3DExtras::QSpriteGridPrivate *self) {
  self->updateTransform();
}

//  QSpriteGrid *Qt3DExtras::QSpriteGridPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSpriteGrid *ritual_ZN10Qt3DExtras18QSpriteGridPrivate6q_funcEv(
    Qt3DExtras::QSpriteGridPrivate *self) {
  return self->q_func();
}

//  const QSpriteGrid *Qt3DExtras::QSpriteGridPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QSpriteGrid *ritual_ZNK10Qt3DExtras18QSpriteGridPrivate6q_funcEv(
    const Qt3DExtras::QSpriteGridPrivate *self) {
  return self->q_func();
}

//  int Qt3DExtras::QSpriteGridPrivate::maxIndex() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10Qt3DExtras18QSpriteGridPrivate8maxIndexEv(
    const Qt3DExtras::QSpriteGridPrivate *self) {
  return self->Qt3DExtras::QSpriteGridPrivate::maxIndex();
}

//  void Qt3DExtras::QSpriteGridPrivate::updateSizes()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DExtras18QSpriteGridPrivate11updateSizesEv(
    Qt3DExtras::QSpriteGridPrivate *self) {
  self->Qt3DExtras::QSpriteGridPrivate::updateSizes();
}

//  void Qt3DExtras::QSpriteGridPrivate::updateTransform()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DExtras18QSpriteGridPrivate15updateTransformEv(
    Qt3DExtras::QSpriteGridPrivate *self) {
  self->Qt3DExtras::QSpriteGridPrivate::updateTransform();
}
