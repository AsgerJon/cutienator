//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qcandbcfileparser_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qcandbcfileparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/qcanmessagedescription.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/qcandbcfileparser.h>
#include <QtSerialBus/private/qcandbcfileparser_p.h>
#include <QtSerialBus/qcanmessagedescription.h>
#include <QtSerialBus/qcansignaldescription.h>
#include <QtSerialBus/qcanuniqueiddescription.h>
#include <QtSerialBus/private/qcanmessagedescription_p.h>
#include <QtSerialBus/private/qcansignaldescription_p.h>
#include <QtCore/QFile>
#include <QtCore/QRegularExpression>
#include <optional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 1132, as _ZN24QCanDbcFileParserPrivate10addWarningEO7QString
inline void QCanDbcFileParserPrivate::addWarning(QString &&warning)
{
    m_warnings.emplace_back(warning);
}

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 358, as _ZN24QCanDbcFileParserPrivate5resetEv
inline void QCanDbcFileParserPrivate::reset()
{
    m_fileName.clear();
    m_error = QCanDbcFileParser::Error::None;
    m_errorString.clear();
    m_warnings.clear();
    m_lineOffset = 0;
    m_isProcessingMessage = false;
    m_seenExtraData = false;
    m_currentMessage = {};
    m_messageDescriptions.clear();
    m_valueDescriptions.clear();
}

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 1137, as _ZN24QCanDbcFileParserPrivate17addCurrentMessageEv
inline void QCanDbcFileParserPrivate::addCurrentMessage()
{
    if (m_isProcessingMessage) {
        auto uid = m_currentMessage.uniqueId();
        if (!m_currentMessage.isValid()) {
            addWarning(QObject::tr("Message description with unique id %1 is skipped "
                                   "because it's not valid.").arg(qToUnderlying(uid)));
        } else if (m_messageDescriptions.contains(uid)) {
            addWarning(QObject::tr("Message description with unique id %1 is skipped "
                                   "because such unique id is already used.").
                       arg(qToUnderlying(uid)));
        } else {
            m_messageDescriptions.insert(uid, m_currentMessage);
        }
        m_currentMessage = {};
        m_isProcessingMessage = false;
    }
}

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 1156, as _ZNK24QCanDbcFileParserPrivate11getMessagesEv
inline QList<QCanMessageDescription> QCanDbcFileParserPrivate::getMessages() const
{
    return QList<QCanMessageDescription>(m_messageDescriptions.cbegin(),
                                         m_messageDescriptions.cend());
}
//  -----------------------------------------------------------------------

//  void QCanDbcFileParserPrivate::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCanDbcFileParserPrivate5resetEv(
    QCanDbcFileParserPrivate *self) {
  self->reset();
}

//  void QCanDbcFileParserPrivate::addCurrentMessage()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCanDbcFileParserPrivate17addCurrentMessageEv(
    QCanDbcFileParserPrivate *self) {
  self->addCurrentMessage();
}

//  QList<QCanMessageDescription> QCanDbcFileParserPrivate::getMessages()
//      const
extern "C" Q_DECL_EXPORT
QList<QCanMessageDescription> *ritual_ZNK24QCanDbcFileParserPrivate11getMessagesEv(
    const QCanDbcFileParserPrivate *self) {
  return new QList<QCanMessageDescription>(self->getMessages());
}

//  QCanDbcFileParserPrivate::~QCanDbcFileParserPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCanDbcFileParserPrivateD1Ev(
    QCanDbcFileParserPrivate *self) {
  delete self;
}
