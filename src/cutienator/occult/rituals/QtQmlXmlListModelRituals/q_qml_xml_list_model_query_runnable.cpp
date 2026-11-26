//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlXmlListModel/6.12.0/QtQmlXmlListModel/private/qqmlxmllistmodel_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQmlXmlListModel/6.12.0/QtQmlXmlListModel/private/qtqmlxmllistmodelglobal_p.h>
#include <QtQmlXmlListModel/QtQmlXmlListModel>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlXmlListModel/6.12.0/QtQmlXmlListModel/private/qqmlxmllistmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/QFuture>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlXmlListModel/private/qqmlxmllistmodel_p.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlxmllistmodel/qqmlxmllistmodel.cpp, line 795, as local:qqmlxmllistmodel.cpp:findIndexOfName
static qsizetype findIndexOfName(const QStringList &elementNames, const QStringView &name,
                                 qsizetype startIndex = 0)
{
    for (auto idx = startIndex; idx < elementNames.size(); ++idx) {
        if (elementNames[idx].startsWith(name))
            return idx;
    }
    return -1;
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

//  from ../qtdeclarative/src/qmlxmllistmodel/qqmlxmllistmodel.cpp, line 897, as _ZN29QQmlXmlListModelQueryRunnable11readSubTreeERK7QStringR16QXmlStreamReaderR8QFlatMapIiS0_St4lessIiE5QListIiES8_IS0_EEPS8_ISt4pairIPvS0_EE
inline void QQmlXmlListModelQueryRunnable::readSubTree(const QString &prefix, QXmlStreamReader &reader,
                                                QFlatMap<int, QString> &results,
                                                QList<std::pair<void *, QString>> *errors)
{
    const QStringList &elementNames = m_job.elementNames;
    const QStringList &attributes = m_job.elementAttributes;
    while (reader.readNextStartElement()) {
        const auto name = reader.name();
        const QString fullName =
                prefix.isEmpty() ? name.toString() : (prefix + QLatin1Char('/') + name.toString());
        qsizetype index = name.isEmpty() ? -1 : findIndexOfName(elementNames, fullName);
        if (index >= 0) {
            // We can have multiple roles with the same element name, but
            // different attributes, so we need to cache the attributes and
            // element text.
            const auto elementAttributes = reader.attributes();
            // We can read text only when the element actually contains it,
            // otherwise it will be an error. It can also be used to check that
            // we've reached the bottom level.
            QString elementText;
            bool elementTextRead = false;
            while (index >= 0) {
                // if the path matches completely, not just starts with, we
                // need to actually extract value
                if (elementNames[index] == fullName) {
                    QString roleResult;
                    const QString &attribute = attributes.at(index);
                    if (!attribute.isEmpty()) {
                        if (elementAttributes.hasAttribute(attribute)) {
                            roleResult = elementAttributes.value(attributes.at(index)).toString();
                        } else {
                            errors->push_back(std::make_pair(m_job.roleQueryErrorId.at(index),
                                                        QLatin1String("Attribute %1 not found")
                                                                .arg(attributes[index])));
                        }
                    } else if (!elementNames.at(index).isEmpty()) {
                        if (!elementTextRead) {
                            elementText =
                                    reader.readElementText(QXmlStreamReader::IncludeChildElements);
                            elementTextRead = true;
                        }
                        roleResult = elementText;
                    }
                    results[index] = roleResult;
                }
                // search for the next role with the same element name
                index = findIndexOfName(elementNames, fullName, index + 1);
            }
            if (!elementTextRead)
                readSubTree(fullName, reader, results, errors);
        } else {
            reader.skipCurrentElement();
        }
    }
}

//  from ../qtdeclarative/src/qmlxmllistmodel/qqmlxmllistmodel.cpp, line 805, as _ZN29QQmlXmlListModelQueryRunnableC1EO24QQmlXmlListModelQueryJob
inline QQmlXmlListModelQueryRunnable::QQmlXmlListModelQueryRunnable(QQmlXmlListModelQueryJob &&job)
    : m_job(std::move(job))
{
    setAutoDelete(true);
}

//  from ../qtdeclarative/src/qmlxmllistmodel/qqmlxmllistmodel.cpp, line 823, as _ZNK29QQmlXmlListModelQueryRunnable6futureEv
inline QFuture<QQmlXmlListModelQueryResult> QQmlXmlListModelQueryRunnable::future() const
{
    return m_promise.future();
}

//  from ../qtdeclarative/src/qmlxmllistmodel/qqmlxmllistmodel.cpp, line 828, as _ZN29QQmlXmlListModelQueryRunnable10doQueryJobEP27QQmlXmlListModelQueryResult
inline void QQmlXmlListModelQueryRunnable::doQueryJob(QQmlXmlListModelQueryResult *currentResult)
{
    Q_ASSERT(m_job.queryId != -1);

    QByteArray data(m_job.data);
    QXmlStreamReader reader;
    reader.addData(data);

    QStringList items = m_job.query.split(QLatin1Char('/'), Qt::SkipEmptyParts);

    while (!reader.atEnd() && !m_promise.isCanceled()) {
        int i = 0;
        while (i < items.size()) {
            if (reader.readNextStartElement()) {
                if (reader.name() == items.at(i)) {
                    if (i != items.size() - 1) {
                        i++;
                        continue;
                    } else {
                        processElement(currentResult, items.at(i), reader);
                    }
                } else {
                    reader.skipCurrentElement();
                }
            }
            if (reader.tokenType() == QXmlStreamReader::Invalid) {
                reader.readNext();
                break;
            } else if (reader.hasError()) {
                reader.raiseError();
                break;
            }
        }
    }
}

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
//  -----------------------------------------------------------------------

//  QQmlXmlListModelQueryRunnable::QQmlXmlListModelQueryRunnable(QQmlXmlListM
//      odelQueryJob &&job)
extern "C" Q_DECL_EXPORT
QQmlXmlListModelQueryRunnable *ritual_ZN29QQmlXmlListModelQueryRunnableC1EO24QQmlXmlListModelQueryJob(
    QQmlXmlListModelQueryJob *job) {
  return new QQmlXmlListModelQueryRunnable(std::move(*job));
}

//  void QQmlXmlListModelQueryRunnable::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlXmlListModelQueryRunnable3runEv(
    QQmlXmlListModelQueryRunnable *self) {
  self->run();
}

//  QFuture<QQmlXmlListModelQueryResult>
//      QQmlXmlListModelQueryRunnable::future() const
extern "C" Q_DECL_EXPORT
QFuture<QQmlXmlListModelQueryResult> *ritual_ZNK29QQmlXmlListModelQueryRunnable6futureEv(
    const QQmlXmlListModelQueryRunnable *self) {
  return new QFuture<QQmlXmlListModelQueryResult>(self->future());
}

//  void
//      QQmlXmlListModelQueryRunnable::doQueryJob(QQmlXmlListModelQueryResult
//      *currentResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlXmlListModelQueryRunnable10doQueryJobEP27QQmlXmlListModelQueryResult(
    QQmlXmlListModelQueryRunnable *self,
    QQmlXmlListModelQueryResult *currentResult) {
  self->doQueryJob(currentResult);
}

//  void
//      QQmlXmlListModelQueryRunnable::processElement(QQmlXmlListModelQueryRe
//      sult *currentResult, const QString &element, QXmlStreamReader
//      &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlXmlListModelQueryRunnable14processElementEP27QQmlXmlListModelQueryResultRK7QStringR16QXmlStreamReader(
    QQmlXmlListModelQueryRunnable *self,
    QQmlXmlListModelQueryResult *currentResult,
    const QString *element,
    QXmlStreamReader *reader) {
  self->processElement(currentResult, *element, *reader);
}

//  void QQmlXmlListModelQueryRunnable::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQmlXmlListModelQueryRunnable3runEv(
    QQmlXmlListModelQueryRunnable *self) {
  self->QQmlXmlListModelQueryRunnable::run();
}

//  a QFuture<QQmlXmlListModelQueryResult> a ritual of
//      QQmlXmlListModelQueryRunnable gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlXmlListModelQueryRunnable__QFuture_QQmlXmlListModelQueryResult(
    QFuture<QQmlXmlListModelQueryResult> *self) {
  delete self;
}
