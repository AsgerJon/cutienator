//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebChannel/6.12.0/QtWebChannel/private/qmetaobjectpublisher_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebChannel/QtWebChannel>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebChannel/6.12.0/QtWebChannel/private/qmetaobjectpublisher_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebChannel/private/qmetaobjectpublisher_p.h>
#include <QtWebChannel/qwebchannel.h>
#include <QtWebChannel/private/qwebchannel_p.h>
#include <QtWebChannel/qwebchannelabstracttransport.h>
#include <QtCore/QEvent>
#if QT_CONFIG(future)
#include <QtCore/QFuture>
#endif
#include <QtCore/QJsonDocument>
#include <QtCore/QDebug>
#include <QtCore/QJsonObject>
#include <QtCore/QJsonArray>
#ifndef QT_NO_JSVALUE
#include <QJSValue>
#endif
#include <QtCore/QUuid>
#include <QtCore/private/qmetaobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebchannel/src/webchannel/qmetaobjectpublisher.cpp, line 228, as _ZN33QWebChannelPropertyChangeNotifier6notifyEP17QPropertyObserverP20QUntypedPropertyData
inline void QWebChannelPropertyChangeNotifier::notify(
        QPropertyObserver *self, QUntypedPropertyData *)
{
    auto This = static_cast<QWebChannelPropertyChangeNotifier*>(self);

    // Use the indirection with Qt::AutoConnection to ensure invocation
    // in the correct thread.
    // Explicitly copy the parameters into the lambda so that this instance can be destroyed after posting a queued
    // invocation. The current design doesn't allow this anyway, but I don't want bad surprises in a possible future
    // commit.
    QMetaObject::invokeMethod(
                This->publisher,
                [publisher=This->publisher, object=This->object, propertyIndex=This->propertyIndex]
    {
        publisher->propertyValueChanged(object, propertyIndex);
    }, Qt::AutoConnection);
}
//  -----------------------------------------------------------------------

//  QWebChannelPropertyChangeNotifier::QWebChannelPropertyChangeNotifier(QMet
//      aObjectPublisher *publisher, const QObject *object, int
//      propertyIndex)
extern "C" Q_DECL_EXPORT
QWebChannelPropertyChangeNotifier *ritual_ZN33QWebChannelPropertyChangeNotifierC1EP20QMetaObjectPublisherPK7QObjecti(
    QMetaObjectPublisher *publisher,
    const QObject *object,
    int propertyIndex) {
  return new QWebChannelPropertyChangeNotifier(
      publisher,
      object,
      propertyIndex);
}

//  void QWebChannelPropertyChangeNotifier::notify(QPropertyObserver *a0,
//      QUntypedPropertyData *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QWebChannelPropertyChangeNotifier6notifyEP17QPropertyObserverP20QUntypedPropertyData(
    QPropertyObserver *a0,
    QUntypedPropertyData *a1) {
  QWebChannelPropertyChangeNotifier::notify(a0, a1);
}
