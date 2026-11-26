//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_tableview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquicktableview_p.h>
#include <QtQuick/private/qquicktableview_p_p.h>
#include <QtCore/qdir.h>
#include <QtCore/qmimedata.h>
#include <QtCore/qtimer.h>
#include <QtQml/private/qqmlincubator_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQmlModels/private/qqmlchangeset_p.h>
#include <QtQmlModels/private/qqmldelegatecomponent_p.h>
#include <QtQmlModels/private/qqmldelegatemodel_p.h>
#include <QtQmlModels/private/qqmldelegatemodel_p_p.h>
#include <QtQuick/qquickitemgrabresult.h>
#include <QtQuick/private/qquickflickable_p_p.h>
#include <QtQuick/private/qquickitemviewfxitem_p_p.h>
#include <QtQuick/private/qquicktaphandler_p.h>
#include <QtCore/qtyperevision.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 1634, as _ZN22QQuickTableViewPrivate9EdgeRangeC1Ev
inline QQuickTableViewPrivate::EdgeRange::EdgeRange()
    : startIndex(kEdgeIndexNotSet)
    , endIndex(kEdgeIndexNotSet)
    , size(0)
{}

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 1640, as _ZN22QQuickTableViewPrivate9EdgeRange13containsIndexEN2Qt4EdgeEi
inline bool QQuickTableViewPrivate::EdgeRange::containsIndex(Qt::Edge edge, int index)
{
    if (startIndex == kEdgeIndexNotSet)
        return false;

    if (endIndex == kEdgeIndexAtEnd) {
        switch (edge) {
        case Qt::LeftEdge:
        case Qt::TopEdge:
            return index <= startIndex;
        case Qt::RightEdge:
        case Qt::BottomEdge:
            return index >= startIndex;
        }
    }

    const int s = std::min(startIndex, endIndex);
    const int e = std::max(startIndex, endIndex);
    return index >= s && index <= e;
}
//  -----------------------------------------------------------------------

//  QQuickTableViewPrivate::EdgeRange::EdgeRange()
extern "C" Q_DECL_EXPORT
QQuickTableViewPrivate::EdgeRange *ritual_ZN22QQuickTableViewPrivate9EdgeRangeC1Ev() {
  return new QQuickTableViewPrivate::EdgeRange();
}

//  bool QQuickTableViewPrivate::EdgeRange::containsIndex(Qt::Edge edge, int
//      index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTableViewPrivate9EdgeRange13containsIndexEN2Qt4EdgeEi(
    QQuickTableViewPrivate::EdgeRange *self,
    Qt::Edge edge,
    int index) {
  return self->containsIndex(edge, index);
}

//  QQuickTableViewPrivate::EdgeRange::~EdgeRange()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate9EdgeRangeD1Ev(
    QQuickTableViewPrivate::EdgeRange *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_tableview)
