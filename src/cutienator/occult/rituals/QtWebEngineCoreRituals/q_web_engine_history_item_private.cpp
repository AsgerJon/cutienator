//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginehistory_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qtwebenginecoreglobal_p.h>
#include <QtWebEngineCore/QtWebEngineCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginehistory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineCore/qwebenginehistory.h>
#include <QtWebEngineCore/private/qwebenginehistory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebengine/src/core/api/qwebenginehistory.cpp, line 17, as _ZN28QWebEngineHistoryItemPrivateC1EPN15QtWebEngineCore24WebContentsAdapterClientEi
inline QWebEngineHistoryItemPrivate::QWebEngineHistoryItemPrivate(
        QtWebEngineCore::WebContentsAdapterClient *client, int index)
    : client(client), index(index)
{
}
//  -----------------------------------------------------------------------

//  QWebEngineHistoryItemPrivate::QWebEngineHistoryItemPrivate(QtWebEngineCor
//      e::WebContentsAdapterClient *client, int index)
extern "C" Q_DECL_EXPORT
QWebEngineHistoryItemPrivate *ritual_ZN28QWebEngineHistoryItemPrivateC1EPN15QtWebEngineCore24WebContentsAdapterClientEi(
    QtWebEngineCore::WebContentsAdapterClient *client,
    int index) {
  return new QWebEngineHistoryItemPrivate(client, index);
}

//  QWebEngineHistoryItemPrivate::~QWebEngineHistoryItemPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWebEngineHistoryItemPrivateD1Ev(
    QWebEngineHistoryItemPrivate *self) {
  delete self;
}
