//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebengineframe_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qlist.h>
#include <QtCore/QWeakPointer>
#include <QtWebEngineCore/QtWebEngineCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/private/qquickwebengineframe_p.h>
#include <QtWebEngineCore/qwebenginescript.h>
#include <QtQml/qqmlengine.h>
#include <QtGui/qpagelayout.h>
#include <QtGui/qpageranges.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebengine/src/webenginequick/api/qquickwebengineframe.cpp, line 20, as _ZN20QQuickWebEngineFrameC1E12QWeakPointerIN15QtWebEngineCore18WebContentsAdapterEEy
inline QQuickWebEngineFrame::QQuickWebEngineFrame(
        QWeakPointer<QtWebEngineCore::WebContentsAdapter> adapter, quint64 id)
    : QWebEngineFrame(std::move(adapter), id)
{
}
//  -----------------------------------------------------------------------

//  void QQuickWebEngineFrame::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickWebEngineFrame20qt_qmlMarker_foreignEv(
    QQuickWebEngineFrame *self) {
  self->qt_qmlMarker_foreign();
}

//  void QQuickWebEngineFrame::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickWebEngineFrame21qt_qmlMarker_extendedEv(
    QQuickWebEngineFrame *self) {
  self->qt_qmlMarker_extended();
}

//  void QQuickWebEngineFrame::runJavaScript(const QString &script, const
//      QJSValue &callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickWebEngineFrame13runJavaScriptERK7QStringRK8QJSValue(
    QQuickWebEngineFrame *self,
    const QString *script,
    const QJSValue *callback) {
  self->runJavaScript(*script, *callback);
}

//  void QQuickWebEngineFrame::runJavaScript(const QString &script, quint32
//      worldId, const QJSValue &callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickWebEngineFrame13runJavaScriptERK7QStringjRK8QJSValue(
    QQuickWebEngineFrame *self,
    const QString *script,
    quint32 worldId,
    const QJSValue *callback) {
  self->runJavaScript(*script, worldId, *callback);
}

//  void QQuickWebEngineFrame::printToPdf(const QJSValue &callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickWebEngineFrame10printToPdfERK8QJSValue(
    QQuickWebEngineFrame *self,
    const QJSValue *callback) {
  self->printToPdf(*callback);
}

//  QQuickWebEngineFrame::QQuickWebEngineFrame(QWeakPointer<QtWebEngineCore::
//      WebContentsAdapter> adapter, quint64 id)
extern "C" Q_DECL_EXPORT
QQuickWebEngineFrame *ritual_ZN20QQuickWebEngineFrameC1E12QWeakPointerIN15QtWebEngineCore18WebContentsAdapterEEy(
    const QWeakPointer<QtWebEngineCore::WebContentsAdapter> *adapter,
    quint64 id) {
  return new QQuickWebEngineFrame(*adapter, id);
}

//  QQuickWebEngineFrame::~QQuickWebEngineFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickWebEngineFrameD1Ev(QQuickWebEngineFrame *self) {
  delete self;
}

//  QList<QQuickWebEngineFrame>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuickWebEngineFrame> *ritual_list_make_QQuickWebEngineFrame() {
  return new QList<QQuickWebEngineFrame>();
}

//  void QList<QQuickWebEngineFrame>::append(const QQuickWebEngineFrame
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuickWebEngineFrame(
    QList<QQuickWebEngineFrame> *self,
    const QQuickWebEngineFrame *element) {
  self->append(*element);
}

//  qsizetype QList<QQuickWebEngineFrame>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuickWebEngineFrame(
    const QList<QQuickWebEngineFrame> *self) {
  return self->size();
}

//  const QQuickWebEngineFrame &QList<QQuickWebEngineFrame>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QQuickWebEngineFrame *ritual_list_at_QQuickWebEngineFrame(
    const QList<QQuickWebEngineFrame> *self,
    long long index) {
  return new QQuickWebEngineFrame(self->at(index));
}

//  QList<QQuickWebEngineFrame>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuickWebEngineFrame(
    QList<QQuickWebEngineFrame> *self) {
  delete self;
}
