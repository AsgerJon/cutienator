//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsgridlayoutengine_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsgridlayoutengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qgraphicsgridlayoutengine_p.h>
#include <QtWidgets/private/qgraphicslayoutitem_p.h>
#include <QtWidgets/private/qgraphicslayout_p.h>
#include <QtWidgets/qgraphicswidget.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/graphicsview/qgraphicsgridlayoutengine.cpp, line 42, as _ZN25QGraphicsGridLayoutEngine12setAlignmentEP19QGraphicsLayoutItem6QFlagsIN2Qt13AlignmentFlagEE
inline void QGraphicsGridLayoutEngine::setAlignment(QGraphicsLayoutItem *graphicsLayoutItem, Qt::Alignment alignment)
{
    if (QGraphicsGridLayoutEngineItem *gridEngineItem = findLayoutItem(graphicsLayoutItem)) {
        gridEngineItem->setAlignment(alignment);
        invalidate();
    }
}

//  from src/widgets/graphicsview/qgraphicsgridlayoutengine.cpp, line 50, as _ZNK25QGraphicsGridLayoutEngine9alignmentEP19QGraphicsLayoutItem
inline Qt::Alignment QGraphicsGridLayoutEngine::alignment(QGraphicsLayoutItem *graphicsLayoutItem) const
{
    if (QGraphicsGridLayoutEngineItem *gridEngineItem = findLayoutItem(graphicsLayoutItem))
        return gridEngineItem->alignment();
    return { };
}

//  from src/widgets/graphicsview/qgraphicsgridlayoutengine.cpp, line 58, as _ZN25QGraphicsGridLayoutEngine16setStretchFactorEP19QGraphicsLayoutItemiN2Qt11OrientationE
inline void QGraphicsGridLayoutEngine::setStretchFactor(QGraphicsLayoutItem *layoutItem, int stretch,
                                         Qt::Orientation orientation)
{
    Q_ASSERT(stretch >= 0);

    if (QGraphicsGridLayoutEngineItem *item = findLayoutItem(layoutItem))
        item->setStretchFactor(stretch, orientation);
}

//  from src/widgets/graphicsview/qgraphicsgridlayoutengine.cpp, line 67, as _ZNK25QGraphicsGridLayoutEngine13stretchFactorEP19QGraphicsLayoutItemN2Qt11OrientationE
inline int QGraphicsGridLayoutEngine::stretchFactor(QGraphicsLayoutItem *layoutItem, Qt::Orientation orientation) const
{
    if (QGraphicsGridLayoutEngineItem *item = findLayoutItem(layoutItem))
        return item->stretchFactor(orientation);
    return 0;
}
//  -----------------------------------------------------------------------

//  QGraphicsGridLayoutEngineItem
//      *QGraphicsGridLayoutEngine::findLayoutItem(QGraphicsLayoutItem
//      *layoutItem) const
extern "C" Q_DECL_EXPORT
QGraphicsGridLayoutEngineItem *ritual_ZNK25QGraphicsGridLayoutEngine14findLayoutItemEP19QGraphicsLayoutItem(
    const QGraphicsGridLayoutEngine *self,
    QGraphicsLayoutItem *layoutItem) {
  return self->findLayoutItem(layoutItem);
}

//  int QGraphicsGridLayoutEngine::indexOf(QGraphicsLayoutItem *item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QGraphicsGridLayoutEngine7indexOfEP19QGraphicsLayoutItem(
    const QGraphicsGridLayoutEngine *self,
    QGraphicsLayoutItem *item) {
  return self->indexOf(item);
}

//  void QGraphicsGridLayoutEngine::setAlignment(QGraphicsLayoutItem
//      *graphicsLayoutItem, Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsGridLayoutEngine12setAlignmentEP19QGraphicsLayoutItem6QFlagsIN2Qt13AlignmentFlagEE(
    QGraphicsGridLayoutEngine *self,
    QGraphicsLayoutItem *graphicsLayoutItem,
    int alignment) {
  self->setAlignment(
      graphicsLayoutItem,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  Qt::Alignment QGraphicsGridLayoutEngine::alignment(QGraphicsLayoutItem
//      *graphicsLayoutItem) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QGraphicsGridLayoutEngine9alignmentEP19QGraphicsLayoutItem(
    const QGraphicsGridLayoutEngine *self,
    QGraphicsLayoutItem *graphicsLayoutItem) {
  return static_cast<int>(self->alignment(graphicsLayoutItem).toInt());
}

//  void QGraphicsGridLayoutEngine::setStretchFactor(QGraphicsLayoutItem
//      *layoutItem, int stretch, Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsGridLayoutEngine16setStretchFactorEP19QGraphicsLayoutItemiN2Qt11OrientationE(
    QGraphicsGridLayoutEngine *self,
    QGraphicsLayoutItem *layoutItem,
    int stretch,
    Qt::Orientation orientation) {
  self->setStretchFactor(layoutItem, stretch, orientation);
}

//  int QGraphicsGridLayoutEngine::stretchFactor(QGraphicsLayoutItem
//      *layoutItem, Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QGraphicsGridLayoutEngine13stretchFactorEP19QGraphicsLayoutItemN2Qt11OrientationE(
    const QGraphicsGridLayoutEngine *self,
    QGraphicsLayoutItem *layoutItem,
    Qt::Orientation orientation) {
  return self->stretchFactor(layoutItem, orientation);
}

//  QGraphicsGridLayoutEngine::~QGraphicsGridLayoutEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsGridLayoutEngineD1Ev(
    QGraphicsGridLayoutEngine *self) {
  delete self;
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
