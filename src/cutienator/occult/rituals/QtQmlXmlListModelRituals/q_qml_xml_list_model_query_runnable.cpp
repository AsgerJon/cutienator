//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlXmlListModel/6.12.0/QtQmlXmlListModel/private/qqmlxmllistmodel_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQmlXmlListModel/6.12.0/QtQmlXmlListModel/private/qtqmlxmllistmodelglobal_p.h>
#include <QtQmlXmlListModel/QtQmlXmlListModel>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlXmlListModel/6.12.0/QtQmlXmlListModel/private/qqmlxmllistmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmlxmllistmodel_p.h"
#include <QtQml/qqmlcontext.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlfile.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qfile.h>
#include <QtCore/qfuturewatcher.h>
#include <QtCore/qtimer.h>
#include <QtCore/qxmlstream.h>
#if QT_CONFIG(qml_network)
#include <QtNetwork/qnetworkreply.h>
#include <QtNetwork/qnetworkrequest.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlxmllistmodel/qqmlxmllistmodel.cpp, line 864, as _ZN29QQmlXmlListModelQueryRunnable14processElementEP27QQmlXmlListModelQueryResultRK7QStringR16QXmlStreamReader
inline void QQmlXmlListModelQueryRunnable::processElement(QQmlXmlListModelQueryResult *currentResult,
                                                   const QString &element, QXmlStreamReader &reader)
{
    if (!reader.isStartElement() || reader.name() != element)
        return;

    const QStringList &elementNames = m_job.elementNames;
    const QStringList &attributes = m_job.elementAttributes;
    QFlatMap<int, QString> results;

    // First of all check all the empty element names. They might have
    // attributes to be read from the current element
    if (!reader.attributes().isEmpty()) {
        for (auto index = 0; index < elementNames.size(); ++index) {
            if (elementNames.at(index).isEmpty() && !attributes.at(index).isEmpty()) {
                const QString &attribute = attributes.at(index);
                if (reader.attributes().hasAttribute(attribute))
                    results[index] = reader.attributes().value(attribute).toString();
            }
        }
    }

    // After that we recursively search for the elements, considering that we
    // can have nested element names in our model, and that the same element
    // can be used multiple types (with different attributes, for example)
    readSubTree(QString(), reader, results, &currentResult->errors);

    if (reader.hasError())
        currentResult->errors.push_back(std::make_pair(this, reader.errorString()));

    currentResult->data << results;
}

//  from ../qtdeclarative/src/qmlxmllistmodel/qqmlxmllistmodel.cpp, line 811, as _ZN29QQmlXmlListModelQueryRunnable3runEv
inline void QQmlXmlListModelQueryRunnable::run()
{
    m_promise.start();
    if (!m_promise.isCanceled()) {
        QQmlXmlListModelQueryResult result;
        result.queryId = m_job.queryId;
        doQueryJob(&result);
        m_promise.addResult(std::move(result));
    }
    m_promise.finish();
}
//  -----------------------------------------------------------------------

//  void QQmlXmlListModelQueryRunnable::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlXmlListModelQueryRunnable3runEv(
    QQmlXmlListModelQueryRunnable *self) {
  self->run();
}
