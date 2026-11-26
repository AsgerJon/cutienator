//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickgridlayoutengine_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutglobal_p.h>
#include <QtQuickLayouts/QtQuickLayouts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickgridlayoutengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickitem.h"
#include <QtQuickLayouts/private/qquickgridlayoutengine_p.h>
#include <QtQuickLayouts/private/qquicklayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicklayouts/qquickgridlayoutengine.cpp, line 11, as _ZN22QQuickGridLayoutEngine12setAlignmentEP10QQuickItem6QFlagsIN2Qt13AlignmentFlagEE
inline void QQuickGridLayoutEngine::setAlignment(QQuickItem *quickItem, Qt::Alignment alignment)
{
    if (QQuickGridLayoutItem *item = findLayoutItem(quickItem)) {
        item->setAlignment(alignment);
        invalidate();
    }
}

//  from ../qtdeclarative/src/quicklayouts/qquickgridlayoutengine.cpp, line 19, as _ZN22QQuickGridLayoutEngine16setStretchFactorEP10QQuickItemiN2Qt11OrientationE
inline void QQuickGridLayoutEngine::setStretchFactor(QQuickItem *quickItem, int stretch,
                                              Qt::Orientation orientation)
{
    Q_ASSERT(stretch >= -1);    // -1 is reset
    if (QGridLayoutItem *item = findLayoutItem(quickItem)) {
        item->setStretchFactor(stretch, orientation);
        invalidate();
    }
}
//  -----------------------------------------------------------------------

//  QQuickGridLayoutEngine::QQuickGridLayoutEngine()
extern "C" Q_DECL_EXPORT
QQuickGridLayoutEngine *ritual_ZN22QQuickGridLayoutEngineC1Ev() {
  return new QQuickGridLayoutEngine();
}

//  int QQuickGridLayoutEngine::indexOf(QQuickItem *item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickGridLayoutEngine7indexOfEP10QQuickItem(
    const QQuickGridLayoutEngine *self,
    QQuickItem *item) {
  return self->indexOf(item);
}

//  QQuickGridLayoutItem *QQuickGridLayoutEngine::findLayoutItem(QQuickItem
//      *layoutItem) const
extern "C" Q_DECL_EXPORT
QQuickGridLayoutItem *ritual_ZNK22QQuickGridLayoutEngine14findLayoutItemEP10QQuickItem(
    const QQuickGridLayoutEngine *self,
    QQuickItem *layoutItem) {
  return self->findLayoutItem(layoutItem);
}

//  void QQuickGridLayoutEngine::setAlignment(QQuickItem *quickItem,
//      Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickGridLayoutEngine12setAlignmentEP10QQuickItem6QFlagsIN2Qt13AlignmentFlagEE(
    QQuickGridLayoutEngine *self,
    QQuickItem *quickItem,
    int alignment) {
  self->setAlignment(
      quickItem,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QQuickGridLayoutEngine::setStretchFactor(QQuickItem *quickItem, int
//      stretch, Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickGridLayoutEngine16setStretchFactorEP10QQuickItemiN2Qt11OrientationE(
    QQuickGridLayoutEngine *self,
    QQuickItem *quickItem,
    int stretch,
    Qt::Orientation orientation) {
  self->setStretchFactor(quickItem, stretch, orientation);
}

//  QQuickGridLayoutEngine::~QQuickGridLayoutEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickGridLayoutEngineD1Ev(QQuickGridLayoutEngine *self) {
  delete self;
}
