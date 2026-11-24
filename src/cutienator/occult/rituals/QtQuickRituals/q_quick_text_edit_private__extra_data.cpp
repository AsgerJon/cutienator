//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextedit_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextedit_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquicktextedit_p.h>
#include <QtQuick/private/qquicktextedit_p_p.h>
#include <QtQuick/private/qquicktextcontrol_p.h>
#include <QtQuick/private/qquicktextdocument_p.h>
#include <QtQuick/qquickwindow.h>
#include <QtQuick/private/qsginternaltextnode_p.h>
#include <QtQuick/private/qquicktextnodeengine_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qvarlengtharray.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qevent.h>
#include <QtGui/qpainter.h>
#include <QtGui/qtextobject.h>
#include <QtGui/qtexttable.h>
#include <QtQml/qqmlinfo.h>
#include <QtQuick/qsgsimplerectnode.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlproperty_p.h>
#include <QtGui/private/qtextengine_p.h>
#include <QtQuick/private/qsgadaptationlayer_p.h>
#include <QtQuick/private/qquickpixmapcache_p.h>
#if QT_CONFIG(accessibility)
#include <QtQuick/private/qquickaccessibleattached_p.h>
#endif
#include <QtQuick/qquicktextdocument.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquicktextedit.cpp, line 2775, as _ZN21QQuickTextEditPrivate9ExtraDataC1Ev
inline QQuickTextEditPrivate::ExtraData::ExtraData()
    : explicitTopPadding(false)
    , explicitLeftPadding(false)
    , explicitRightPadding(false)
    , explicitBottomPadding(false)
    , implicitResize(true)
{
}
//  -----------------------------------------------------------------------

//  QQuickTextEditPrivate::ExtraData::ExtraData()
extern "C" Q_DECL_EXPORT
QQuickTextEditPrivate::ExtraData *ritual_ZN21QQuickTextEditPrivate9ExtraDataC1Ev() {
  return new QQuickTextEditPrivate::ExtraData();
}

//  QQuickTextEditPrivate::ExtraData::~ExtraData()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate9ExtraDataD1Ev(
    QQuickTextEditPrivate::ExtraData *self) {
  delete self;
}
