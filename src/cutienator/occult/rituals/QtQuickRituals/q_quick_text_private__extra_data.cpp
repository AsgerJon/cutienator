//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktext_p_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktext_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquicktext_p.h>
#include <QtQuick/private/qquicktext_p_p.h>
#include <QtQml/private/qqmldebugserviceinterfaces_p.h>
#include <QtQml/private/qqmldebugconnector_p.h>
#include <QtQuick/private/qsgcontext_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQuick/private/qsgadaptationlayer_p.h>
#include <QtQuick/private/qsginternaltextnode_p.h>
#include <QtQuick/private/qquicktextutil_p.h>
#include <QtQuick/private/qsgtexture_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtGui/qevent.h>
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtGui/qpainter.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/qtextobject.h>
#include <QtGui/qtextcursor.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qinputmethod.h>
#include <QtGui/private/qtextengine_p.h>
#include <QtQuick/private/qquickstyledtext_p.h>
#include <QtQuick/private/qquickpixmap_p.h>
#include <QtCore/qmath.h>
#include <limits.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquicktext.cpp, line 71, as _ZN17QQuickTextPrivate9ExtraDataC1Ev
inline QQuickTextPrivate::ExtraData::ExtraData()
    : padding(0)
    , topPadding(0)
    , leftPadding(0)
    , rightPadding(0)
    , bottomPadding(0)
    , explicitTopPadding(false)
    , explicitLeftPadding(false)
    , explicitRightPadding(false)
    , explicitBottomPadding(false)
    , lineHeight(1.0)
    , doc(nullptr)
    , minimumPixelSize(12)
    , minimumPointSize(12)
    , maximumLineCount(INT_MAX)
    , renderTypeQuality(QQuickText::DefaultRenderTypeQuality)
    , lineHeightValid(false)
    , lineHeightMode(QQuickText::ProportionalHeight)
    , fontSizeMode(QQuickText::FixedSize)
{
}
//  -----------------------------------------------------------------------

//  QQuickTextPrivate::ExtraData::ExtraData()
extern "C" Q_DECL_EXPORT
QQuickTextPrivate::ExtraData *ritual_ZN17QQuickTextPrivate9ExtraDataC1Ev() {
  return new QQuickTextPrivate::ExtraData();
}

//  QQuickTextPrivate::ExtraData::~ExtraData()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextPrivate9ExtraDataD1Ev(
    QQuickTextPrivate::ExtraData *self) {
  delete self;
}
