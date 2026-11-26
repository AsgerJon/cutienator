//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qspritesheetitem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qspritesheetitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qspritesheetitem.h>
#include <Qt3DExtras/private/qspritesheetitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/defaults/qspritesheetitem.cpp, line 14, as _ZN10Qt3DExtras23QSpriteSheetItemPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QSpriteSheetItemPrivate::QSpriteSheetItemPrivate()
    : QNodePrivate()
    , m_x(0)
    , m_y(0)
    , m_width(0)
    , m_height(0)
{

}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  Qt3DExtras::QSpriteSheetItemPrivate::QSpriteSheetItemPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSpriteSheetItemPrivate *ritual_ZN10Qt3DExtras23QSpriteSheetItemPrivateC1Ev() {
  return new Qt3DExtras::QSpriteSheetItemPrivate();
}

//  QSpriteSheetItem *Qt3DExtras::QSpriteSheetItemPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSpriteSheetItem *ritual_ZN10Qt3DExtras23QSpriteSheetItemPrivate6q_funcEv(
    Qt3DExtras::QSpriteSheetItemPrivate *self) {
  return self->q_func();
}

//  const QSpriteSheetItem *Qt3DExtras::QSpriteSheetItemPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QSpriteSheetItem *ritual_ZNK10Qt3DExtras23QSpriteSheetItemPrivate6q_funcEv(
    const Qt3DExtras::QSpriteSheetItemPrivate *self) {
  return self->q_func();
}
