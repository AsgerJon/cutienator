//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qcandbcfileparser_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qcandbcfileparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qregularexpression.h>
#include <QtSerialBus/qcanmessagedescription.h>
#include <QtCore/qstringview.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 338, as local:qcandbcfileparser.cpp:kQtDummySignal
static const auto kQtDummySignal = u"Qt Dummy Signal"_s;

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 340, as local:qcandbcfileparser.cpp:kMessageDef
static constexpr auto kMessageDef = "BO_ "_L1;

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 341, as local:qcandbcfileparser.cpp:kSignalDef
static constexpr auto kSignalDef = "SG_ "_L1;

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 342, as local:qcandbcfileparser.cpp:kSigValTypeDef
static constexpr auto kSigValTypeDef = "SIG_VALTYPE_ "_L1;

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 343, as local:qcandbcfileparser.cpp:kCommentDef
static constexpr auto kCommentDef = "CM_ "_L1;

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 344, as local:qcandbcfileparser.cpp:kExtendedMuxDef
static constexpr auto kExtendedMuxDef = "SG_MUL_VAL_ "_L1;

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 345, as local:qcandbcfileparser.cpp:kValDef
static constexpr auto kValDef = "VAL_ "_L1;

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 347, as local:qcandbcfileparser.cpp:kUnsignedIntRegExp
static constexpr auto kUnsignedIntRegExp = "\\d+"_L1;

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 348, as local:qcandbcfileparser.cpp:kDoubleRegExp
static constexpr auto kDoubleRegExp = "[+-]?\\d+((.\\d*)?([eE][+-]?\\d+)?)?"_L1;

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 349, as local:qcandbcfileparser.cpp:kDbcIdentRegExp
static constexpr auto kDbcIdentRegExp = "[_[:alpha:]][_[:alnum:]]+"_L1;

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 350, as local:qcandbcfileparser.cpp:kOneOrMoreSpaceRegExp
static constexpr auto kOneOrMoreSpaceRegExp = "[ ]+"_L1;

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 351, as local:qcandbcfileparser.cpp:kMaybeSpaceRegExp
static constexpr auto kMaybeSpaceRegExp = "[ ]*"_L1;

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 352, as local:qcandbcfileparser.cpp:kMuxIndicatorRegExp
static constexpr auto kMuxIndicatorRegExp = "M|m\\d+M?"_L1;

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 353, as local:qcandbcfileparser.cpp:kByteOrderRegExp
static constexpr auto kByteOrderRegExp = "0|1"_L1;

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 354, as local:qcandbcfileparser.cpp:kValueTypeRegExp
static constexpr auto kValueTypeRegExp = "\\+|\\-"_L1;

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 356, as local:qcandbcfileparser.cpp:kCharStrRegExp
static constexpr auto kCharStrRegExp = "((?![\\\"\\\\])\\P{Cc})*"_L1;

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 400, as local:qcandbcfileparser.cpp:ReadData
struct ReadData
{
    qsizetype index;
    QStringView result;
};

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 505, as local:qcandbcfileparser.cpp:extractUniqueId
static std::optional<QtCanBus::UniqueId> extractUniqueId(QStringView view)
{
    bool ok = false;
    const uint value = view.toUInt(&ok);
    if (ok)
        return QtCanBus::UniqueId{value & 0x1FFFFFFF};
    return std::nullopt;
}

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 446, as _ZN24QCanDbcFileParserPrivate11processLineE11QStringView
inline bool QCanDbcFileParserPrivate::processLine(const QStringView line)
{
    QStringView data = line;
    m_lineOffset = 0;

    auto handleParsingError = [this](QLatin1StringView section) {
        m_error = QCanDbcFileParser::Error::Parsing;
        m_errorString = !m_fileName.isEmpty()
                ? QObject::tr("Failed to parse file %1. Unexpected position "
                              "of %2 section.").arg(m_fileName, section)
                : QObject::tr("Failed to parse input data. Unexpected position "
                              "of %1 section.").arg(section);
    };

    if (data.startsWith(kMessageDef)) {
        if (m_seenExtraData) {
            // Unexpected position of message description
            handleParsingError(kMessageDef);
            return false;
        }
        addCurrentMessage();
        if (!parseMessage(data))
            return false;
    }
    // signal definitions can be on the same line as message definition,
    // or on a separate line
    data = data.sliced(m_lineOffset).trimmed();
    while (data.startsWith(kSignalDef)) {
        if (!m_isProcessingMessage || m_seenExtraData) {
            // Unexpected position of signal description
            handleParsingError(kSignalDef);
            return false;
        }
        if (!parseSignal(data))
            return false;
        data = data.sliced(m_lineOffset).trimmed();
    }
    // If we detect one of the following lines, then message description is
    // finished. We also assume that we can have only one key at each line.
    if (data.startsWith(kSigValTypeDef)) {
        m_seenExtraData = true;
        addCurrentMessage();
        parseSignalType(data);
    } else if (data.startsWith(kCommentDef)) {
        m_seenExtraData = true;
        addCurrentMessage();
        parseComment(data);
    } else if (data.startsWith(kExtendedMuxDef)) {
        m_seenExtraData = true;
        addCurrentMessage();
        parseExtendedMux(data);
    } else if (data.startsWith(kValDef)) {
        m_seenExtraData = true;
        addCurrentMessage();
        parseValueDescriptions(data);
    }
    return true;
}

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 1067, as _ZN24QCanDbcFileParserPrivate29postProcessSignalMultiplexingEv
inline void QCanDbcFileParserPrivate::postProcessSignalMultiplexing()
{
    // For the case of simple multiplexing we need to do the following for
    // every message description:
    // 1. Find the multiplexor signal
    // 2. Replace all kQtDummySignal entries with the name of the multiplexor
    // 3. While doing so, check if we have any signals with type
    //    SwitchAndSignal. This will mean that extended multiplexing is used
    // 4. Also detect conditions when we have more than one multiplexor signal.
    //    This is an error as well, and message description should be discarded.

    QList<QtCanBus::UniqueId> uidsToRemove;

    for (auto &messageDesc : m_messageDescriptions) {
        bool useExtendedMux = false;
        QString multiplexorSignal;
        auto &signalDescriptions = QCanMessageDescriptionPrivate::get(messageDesc)->messageSignals;
        for (const auto &signalDesc : std::as_const(signalDescriptions)) {
            if (signalDesc.multiplexState() == QtCanBus::MultiplexState::MultiplexorSwitch) {
                if (multiplexorSignal.isEmpty()) {
                    multiplexorSignal = signalDesc.name();
                } else {
                    // invalid config
                    multiplexorSignal.clear();
                    uidsToRemove.push_back(messageDesc.uniqueId());
                    break;
                }
            } else if (signalDesc.multiplexState() == QtCanBus::MultiplexState::SwitchAndSignal) {
                // extended multiplexing
                useExtendedMux = true;
            }
        }
        if (!useExtendedMux && !multiplexorSignal.isEmpty()) {
            // iterate through all signal descriptions and update kQtDummySignal
            for (auto &signalDesc : signalDescriptions) {
                if (signalDesc.multiplexState() == QtCanBus::MultiplexState::MultiplexedSignal) {
                    auto &muxValues = QCanSignalDescriptionPrivate::get(signalDesc)->muxSignals;
                    auto val = muxValues.value(kQtDummySignal);
                    muxValues.remove(kQtDummySignal);
                    muxValues.insert(multiplexorSignal, val);
                }
            }
        } else if (useExtendedMux) {
            // Iterate through all signal descriptions and check that we do
            // not have any kQtDummySignal entries. It such entry exists, this
            // means that there were errors while parsing extended multiplexing
            // table, and this message description is invalid
            for (const auto &signalDesc : std::as_const(signalDescriptions)) {
                const auto muxSignals = signalDesc.multiplexSignals();
                if (muxSignals.contains(kQtDummySignal)) {
                    uidsToRemove.push_back(messageDesc.uniqueId());
                    break;
                }
            }
        }
    }

    for (const auto &uid : std::as_const(uidsToRemove)) {
        m_messageDescriptions.remove(uid);
        addWarning(QObject::tr("Message description with unique id %1 is skipped because "
                               "it has invalid multiplexing description.").
                   arg(qToUnderlying(uid)));
    }
}

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 639, as _ZN24QCanDbcFileParserPrivate13extractSignalERK23QRegularExpressionMatch
inline QCanSignalDescription QCanDbcFileParserPrivate::extractSignal(const QRegularExpressionMatch &match)
{
    Q_ASSERT(match.hasMatch());
    QCanSignalDescription desc;
    desc.setName(match.captured(u"name"_s));

    bool ok = false;

    if (match.hasCaptured(u"mux"_s)) {
        const auto muxStr = match.capturedView(u"mux"_s);
        if (muxStr == u"M"_s) {
            desc.setMultiplexState(QtCanBus::MultiplexState::MultiplexorSwitch);
        } else if (muxStr.endsWith(u"M"_s, Qt::CaseSensitive)) {
            desc.setMultiplexState(QtCanBus::MultiplexState::SwitchAndSignal);
            const auto val = muxStr.sliced(1, muxStr.size() - 2).toUInt(&ok);
            if (!ok) {
                addWarning(QObject::tr("Failed to parse multiplexor value for signal %1").
                           arg(desc.name()));
                return {};
            }
            // We have the value, but we do not really know the multiplexor
            // switch name. To know it, we potentially need to parse all signals
            // for the message. So for now we just create a dummy entry, and
            // the actual signal name will be updated later;
            desc.addMultiplexSignal(kQtDummySignal, val);
        } else {
            desc.setMultiplexState(QtCanBus::MultiplexState::MultiplexedSignal);
            const auto val = muxStr.sliced(1).toUInt(&ok);
            if (!ok) {
                addWarning(QObject::tr("Failed to parse multiplexor value for signal %1").
                           arg(desc.name()));
                return {};
            }
            // Same as above
            desc.addMultiplexSignal(kQtDummySignal, val);
        }
    }

    const uint startBit = match.capturedView(u"startBit"_s).toUInt(&ok);
    if (ok) {
        desc.setStartBit(startBit);
    } else {
        addWarning(QObject::tr("Failed to parse start bit for signal %1").arg(desc.name()));
        return {};
    }

    const uint bitLength = match.capturedView(u"sigSize"_s).toUInt(&ok);
    if (ok) {
        desc.setBitLength(bitLength);
    } else {
        addWarning(QObject::tr("Failed to parse bit length for signal %1").arg(desc.name()));
        return {};
    }

    // 0 = BE; 1 = LE
    const auto endian = match.capturedView(u"byteOrder"_s) == u"0"_s
            ? QSysInfo::Endian::BigEndian : QSysInfo::Endian::LittleEndian;
    desc.setDataEndian(endian);

    // + = unsigned; - = signed
    const auto dataFormat = match.capturedView(u"valueType"_s) == u"+"_s
            ? QtCanBus::DataFormat::UnsignedInteger : QtCanBus::DataFormat::SignedInteger;
    desc.setDataFormat(dataFormat);

    const double factor = match.capturedView(u"factor"_s).toDouble(&ok);
    if (ok) {
        desc.setFactor(factor);
    } else {
        addWarning(QObject::tr("Failed to parse factor for signal %1").arg(desc.name()));
        return {};
    }

    const double offset = match.capturedView(u"offset"_s).toDouble(&ok);
    if (ok) {
        desc.setOffset(offset);
    } else {
        addWarning(QObject::tr("Failed to parse offset for signal %1").arg(desc.name()));
        return {};
    }

    const double min = match.capturedView(u"min"_s).toDouble(&ok);
    if (ok) {
        const double max = match.capturedView(u"max"_s).toDouble(&ok);
        if (ok)
            desc.setRange(min, max);
    }
    if (!ok) {
        addWarning(QObject::tr("Failed to parse value range from signal %1").arg(desc.name()));
        return {};
    }

    desc.setPhysicalUnit(match.captured(u"unit"_s));
    desc.setReceiver(match.captured(u"receiver"_s));

    return desc;
}

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 816, as _ZN24QCanDbcFileParserPrivate12parseCommentE11QStringView
inline void QCanDbcFileParserPrivate::parseComment(const QStringView data)
{
    // The comment for message or signal description is represented by the
    // following pattern:
    //      CM_ (BO_ message_id char_string | SG_ message_id signal_name char_string);

    // %1 commentDef
    // %2 maybeSpace
    // %3 messageDef
    // %4 signalDef
    // %5 oneOrMoreSpace
    // %6 unsignedInt
    // %7 DbcIdentifier
    // %8 charStr
    const QString regExStr =
            "%1%2(?<type>(%3|%4))%2(?<messageId>%6)%5((?<sigName>%7)%5)?\"(?<comment>%8)\"%2;"_L1.
            arg(kCommentDef, kMaybeSpaceRegExp, kMessageDef, kSignalDef, kOneOrMoreSpaceRegExp,
                kUnsignedIntRegExp, kDbcIdentRegExp, kCharStrRegExp);
    const QRegularExpression commentRegExp(regExStr);

    const auto match = commentRegExp.matchView(data);
    if (!match.hasMatch()) {
        // no warning here, as we ignore some "general" comments, and parse only
        // comments related to messages and signals
        m_lineOffset = data.size();
        return;
    }

    m_lineOffset = match.capturedEnd(0);

    const auto type = match.capturedView(u"type"_s);

    const auto uidOptional = extractUniqueId(match.capturedView(u"messageId"_s));
    if (!uidOptional) {
        addWarning(QObject::tr("Failed to parse frame id from string %1").arg(data));
        return;
    }

    const QtCanBus::UniqueId uid = uidOptional.value();
    auto messageDesc = m_messageDescriptions.value(uid);
    if (!messageDesc.isValid()) {
        addWarning(QObject::tr("Failed to find message description for unique id %1. "
                               "Skipping string %2").arg(qToUnderlying(uid)).arg(data));
        return;
    }

    if (type == kMessageDef) {
        const QString comment = match.captured(u"comment"_s);
        messageDesc.setComment(comment);
        m_messageDescriptions.insert(uid, messageDesc);
    } else if (type == kSignalDef) {
        const QString sigName = match.captured(u"sigName"_s);
        auto signalDesc = messageDesc.signalDescriptionForName(sigName);
        if (signalDesc.isValid()) {
            const QString comment = match.captured(u"comment"_s);
            signalDesc.setComment(comment);
            messageDesc.addSignalDescription(signalDesc);
            m_messageDescriptions.insert(uid, messageDesc);
        } else {
            addWarning(QObject::tr("Failed to find signal description for signal %1. "
                                   "Skipping string %2").arg(sigName, data));
        }
    }
}

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 519, as _ZN24QCanDbcFileParserPrivate12parseMessageE11QStringView
inline bool QCanDbcFileParserPrivate::parseMessage(const QStringView data)
{
    // The regexp matches the following definition:
    // BO_ message_id message_name ':' message_size transmitter
    // also considering the fact that spaces around ':' seem to be optional, and
    // allowing more than one space between parts.

    // %1 - messageDef
    // %2 - maybeSpace
    // %3 - unsignedInt
    // %4 - oneOrMoreSpace
    // %5 - DbcIdentifier
    static const QString regExStr =
            "%1%2(?<messageId>%3)%4(?<name>%5)%2:%2(?<size>%3)%4(?<transmitter>%5)"_L1.
            arg(kMessageDef, kMaybeSpaceRegExp, kUnsignedIntRegExp, kOneOrMoreSpaceRegExp,
                kDbcIdentRegExp);
    static const QRegularExpression messageRegExp(regExStr);

    m_isProcessingMessage = false;
    const auto match = messageRegExp.matchView(data);
    if (match.hasMatch()) {
        m_currentMessage = extractMessage(match);
        // can't check for isValid() here, because demands signal descriptions
        if (!m_currentMessage.name().isEmpty()) {
            m_isProcessingMessage = true;
        } else {
            addWarning(QObject::tr("Failed to parse message description from "
                                   "string %1").arg(data));
        }
        m_lineOffset = match.capturedEnd(0);
    } else {
        addWarning(QObject::tr("Failed to find message description in string %1").arg(data));
        m_lineOffset = data.size(); // skip this string
    }
    return true;
}

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 736, as _ZN24QCanDbcFileParserPrivate15parseSignalTypeE11QStringView
inline void QCanDbcFileParserPrivate::parseSignalType(const QStringView data)
{
    // The regexp should match the following pattern:
    //      SIG_VALTYPE_ message_id signal_name signal_extended_value_type ;
    // We also need to consider the fact that we can potentially allow more
    // spaces between parts.

    // %1 sigValTypeDef
    // %2 maybeSpace
    // %3 unsignedInt
    // %4 oneOrMoreSpace
    // %5 DbcIdentifier
    const QString regExStr =
            "%1%2(?<messageId>%3)%4(?<sigName>%5)%2:%2(?<type>%3)%2;"_L1.
            arg(kSigValTypeDef, kMaybeSpaceRegExp, kUnsignedIntRegExp,
                kOneOrMoreSpaceRegExp, kDbcIdentRegExp);
    const QRegularExpression sigValTypeRegEx(regExStr);

    const auto match = sigValTypeRegEx.matchView(data);
    if (!match.hasMatch()) {
        m_lineOffset = data.size();
        addWarning(QObject::tr("Failed to find signal value type description in string %1").
                   arg(data));
        return;
    }

    m_lineOffset = match.capturedEnd(0);

    const auto uidOptional = extractUniqueId(match.capturedView(u"messageId"_s));
    if (!uidOptional) {
        addWarning(QObject::tr("Failed to parse frame id from string %1").arg(data));
        return;
    }

    const QtCanBus::UniqueId uid = uidOptional.value();
    auto msgDesc = m_messageDescriptions.value(uid);
    if (msgDesc.isValid()) {
        const QString sigName = match.captured(u"sigName"_s);
        auto sigDesc = msgDesc.signalDescriptionForName(sigName);
        if (sigDesc.isValid()) {
            bool ok = false;
            const auto type = match.capturedView(u"type").toUInt(&ok);
            if (ok) {
                bool sigDescChanged = false;
                switch (type) {
                case 0: /* signed or unsigned integer */
                    // do nothing, as we already have signed/unsinged integer
                    // based on "SG_ " string
                    break;
                case 1: /* 32-bit IEEE-float */
                    sigDesc.setDataFormat(QtCanBus::DataFormat::Float);
                    sigDesc.setBitLength(32);
                    sigDescChanged = true;
                    break;
                case 2: /* 64-bit IEEE-double */
                    sigDesc.setDataFormat(QtCanBus::DataFormat::Double);
                    sigDesc.setBitLength(64);
                    sigDescChanged = true;
                    break;
                default:
                    // invalid value
                    break;
                }
                if (sigDescChanged) {
                    msgDesc.addSignalDescription(sigDesc);
                    m_messageDescriptions.insert(msgDesc.uniqueId(), msgDesc);
                }
            } else {
                addWarning(QObject::tr("Failed to parse data type from string %1").arg(data));
            }
        } else {
            addWarning(QObject::tr("Failed to find signal description for signal %1. "
                                   "Skipping string %2").arg(sigName, data));
        }
    } else {
        addWarning(QObject::tr("Failed to find message description for unique id %1. "
                               "Skipping string %2").arg(qToUnderlying(uid)).arg(data));
    }
}

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 881, as _ZN24QCanDbcFileParserPrivate16parseExtendedMuxE11QStringView
inline void QCanDbcFileParserPrivate::parseExtendedMux(const QStringView data)
{
    // The extended multiplexing is defined by the following pattern:
    //      SG_MUL_VAL_ message_id multiplexed_signal_name
    //      multiplexor_switch_name multiplexor_value_ranges ;
    // Here multiplexor_value_ranges consists of multiple ranges, separated
    // by a whitespace, and one range is defined as follows:
    //      multiplexor_value_range = unsigned_integer - unsigned_integer

    // %1 extendedMuxDef
    // %2 maybeSpace
    // %3 unsignedInt
    // %4 oneOrMoreSpace
    // %5 DbcIdentifier
    const QString regExStr =
            "%1%2(?<messageId>%3)%4(?<multiplexedSignal>%5)%4(?<multiplexorSwitch>%5)%4"
            "(?<firstRange>%3%2-%2%3)(%2,%2%3%2-%2%3)*%2;"_L1.
            arg(kExtendedMuxDef, kMaybeSpaceRegExp, kUnsignedIntRegExp, kOneOrMoreSpaceRegExp,
                kDbcIdentRegExp);
    const QRegularExpression extendedMuxRegExp(regExStr);

    const auto match = extendedMuxRegExp.matchView(data);
    if (!match.hasMatch()) {
        m_lineOffset = data.size();
        addWarning(QObject::tr("Failed to find extended multiplexing description in string %1").
                   arg(data));
        return;
    }

    m_lineOffset = match.capturedEnd(0);

    const auto uidOptional = extractUniqueId(match.capturedView(u"messageId"_s));
    if (!uidOptional) {
        addWarning(QObject::tr("Failed to parse frame id from string %1").arg(data));
        return;
    }

    const QtCanBus::UniqueId uid = uidOptional.value();
    auto messageDesc = m_messageDescriptions.value(uid);
    if (!messageDesc.isValid()) {
        addWarning(QObject::tr("Failed to find message description for unique id %1. "
                               "Skipping string %2").arg(qToUnderlying(uid)).arg(data));
        return;
    }

    const QString multiplexedSignalName = match.captured(u"multiplexedSignal"_s);
    const QString multiplexorSwitchName = match.captured(u"multiplexorSwitch"_s);

    auto multiplexedSignal = messageDesc.signalDescriptionForName(multiplexedSignalName);
    auto multiplexorSwitch = messageDesc.signalDescriptionForName(multiplexorSwitchName);

    if (!multiplexedSignal.isValid() || !multiplexorSwitch.isValid()) {
        const QString invalidName = multiplexedSignal.isValid() ? multiplexorSwitchName
                                                                : multiplexedSignalName;
        addWarning(QObject::tr("Failed to find signal description for signal %1. "
                               "Skipping string %2").arg(invalidName, data));
        return;
    }

    auto signalRanges = multiplexedSignal.multiplexSignals();
    signalRanges.remove(kQtDummySignal); // dummy signal not needed anymore

    QCanSignalDescription::MultiplexValues rangeValues;
    auto rangeView = match.capturedView(u"firstRange"_s);
    const auto sepIdx = rangeView.indexOf(u'-');
    if (sepIdx != -1) {
        const auto min = rangeView.first(sepIdx).trimmed().toUInt();
        const auto max = rangeView.sliced(sepIdx + 1).trimmed().toUInt();
        rangeValues.push_back({min, max});
    }

    // We can have an arbitrary amount of ranges, so we can't use capture groups
    // to capture them. But we know that they follow a specific pattern (because
    // the full string matched the regexp). So we need to parse the rest of the
    // matched string manually
    const auto totalEnd = match.capturedEnd(0); // including the ';'
    const auto firstRangeEnd = match.capturedEnd(u"firstRange"_s);
    const auto len = totalEnd - firstRangeEnd - 1;
    if (len > 0) {
        const auto otherRangesView = data.sliced(firstRangeEnd, len).trimmed();
        const QStringTokenizer parts = otherRangesView.tokenize(u',', Qt::SkipEmptyParts);
        for (const QStringView range : parts) {
            const auto sepIdx = range.indexOf(u'-');
            if (sepIdx != -1) {
                const auto min = range.first(sepIdx).trimmed().toUInt();
                const auto max = range.sliced(sepIdx + 1).trimmed().toUInt();
                rangeValues.push_back({min, max});
            }
        }
    }

    if (!rangeValues.isEmpty())
        signalRanges.insert(multiplexorSwitchName, rangeValues);
    else
        signalRanges.remove(multiplexorSwitchName);

    // update the value
    multiplexedSignal.setMultiplexSignals(signalRanges);
    messageDesc.addSignalDescription(multiplexedSignal);
    m_messageDescriptions.insert(uid, messageDesc);
}

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 983, as _ZN24QCanDbcFileParserPrivate22parseValueDescriptionsE11QStringView
inline void QCanDbcFileParserPrivate::parseValueDescriptions(const QStringView data)
{
    // The regexp should match the following pattern:
    //      VAL_ message_id signal_name { value_description };
    // Here the value_description is defined as follows
    //      value_description = unsigned_int char_string

    // %1 valDef
    // %2 maybeSpace
    // %3 unsignedInt
    // %4 oneOrMoreSpace
    // %5 DbcIdentifier
    // %6 charStr
    const QString regExStr =
            "%1%2(?<messageId>%3)%4(?<signalName>%5)(%4%3%4\"(%6)\")+%2;"_L1.
            arg(kValDef, kMaybeSpaceRegExp, kUnsignedIntRegExp, kOneOrMoreSpaceRegExp,
                kDbcIdentRegExp, kCharStrRegExp);

    const QRegularExpression valueDescRegExp(regExStr);

    const auto match = valueDescRegExp.matchView(data);
    if (!match.hasMatch()) {
        m_lineOffset = data.size();
        addWarning(QObject::tr("Failed to parse value description from string %1").arg(data));
        return;
    }

    m_lineOffset = match.capturedEnd(0);

    const auto uidOptional = extractUniqueId(match.capturedView(u"messageId"_s));
    if (!uidOptional) {
        addWarning(QObject::tr("Failed to parse value description from string %1").arg(data));
        return;
    }

    const QtCanBus::UniqueId uid = uidOptional.value();
    // Check if the message exists
    const auto messageDesc = m_messageDescriptions.value(uid);
    if (!messageDesc.isValid()) {
        addWarning(QObject::tr("Failed to find message description for unique id %1. "
                               "Skipping string %2").arg(qToUnderlying(uid)).arg(data));
        return;
    }

    // Check if the signal exists within the message
    const QString signalName = match.captured(u"signalName"_s);
    if (!messageDesc.signalDescriptionForName(signalName).isValid()) {
        addWarning(QObject::tr("Failed to find signal description for signal %1. "
                               "Skipping string %2").arg(signalName, data));
        return;
    }

    // We can have an arbitrary amount of value descriptions, so we can't use
    // capture groups to capture them. But we know that they follow a specific
    // pattern (because the full string matched the regexp). So we need to parse
    // the rest of the matched string manually
    const auto totalEnd = match.capturedEnd(0); // including the ';'
    const auto signalNameEnd = match.capturedEnd(u"signalName"_s);
    const auto len = totalEnd - signalNameEnd - 1;
    if (len > 0) {
        auto signalDescriptionsView = data.sliced(signalNameEnd, len).trimmed();
        while (signalDescriptionsView.size()) {
            const auto spacePos = signalDescriptionsView.indexOf(u' ');
            if (spacePos == -1)
                break;
            bool ok = false;
            const auto value = signalDescriptionsView.sliced(0, spacePos).toUInt(&ok);
            if (!ok)
                break;
            const auto firstQuotePos = signalDescriptionsView.indexOf(u'"', spacePos + 1);
            if (firstQuotePos == -1)
                break;
            const auto nextQuotePos = signalDescriptionsView.indexOf(u'"', firstQuotePos + 1);
            if (nextQuotePos == -1)
                break;
            const auto description = signalDescriptionsView.sliced(
                        firstQuotePos + 1, nextQuotePos - firstQuotePos - 1);

            m_valueDescriptions[uid][signalName].insert(value, description.toString());
            signalDescriptionsView = signalDescriptionsView.sliced(nextQuotePos + 1).trimmed();
        }
    }
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

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 377, as _ZN24QCanDbcFileParserPrivate9parseFileERK7QString
inline bool QCanDbcFileParserPrivate::parseFile(const QString &fileName)
{
    QFile f(fileName);
    if (!f.open(QIODevice::ReadOnly)) {
        m_error = QCanDbcFileParser::Error::FileReading;
        m_errorString = f.errorString();
        return false;
    }
    m_fileName = fileName;
    m_seenExtraData = false;

    while (!f.atEnd()) {
        const QString str = QString::fromUtf8(f.readLine().trimmed());
        if (!processLine({str.constData(), str.size()})) // also sets the error properly
            return false;
    }
    addCurrentMessage(); // check if we need to add the message
    // now when we parsed the whole file, we can verify the signal multiplexing
    postProcessSignalMultiplexing();

    return true;
}

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 556, as _ZN24QCanDbcFileParserPrivate14extractMessageERK23QRegularExpressionMatch
inline QCanMessageDescription
QCanDbcFileParserPrivate::extractMessage(const QRegularExpressionMatch &match)
{
    Q_ASSERT(match.hasMatch());
    QCanMessageDescription desc;
    desc.setName(match.captured(u"name"_s));

    const auto id = extractUniqueId(match.capturedView(u"messageId"_s));
    if (id.has_value()) {
        desc.setUniqueId(id.value());
    } else {
        addWarning(QObject::tr("Failed to parse frame id for message %1").arg(desc.name()));
        return {};
    }

    bool ok = false;
    const auto size = match.capturedView(u"size"_s).toUInt(&ok);
    if (ok) {
        desc.setSize(size);
    } else {
        addWarning(QObject::tr("Failed to parse size for message %1").arg(desc.name()));
        return {};
    }

    desc.setTransmitter(match.captured(u"transmitter"_s));

    return desc;
}

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 590, as _ZN24QCanDbcFileParserPrivate11parseSignalE11QStringView
inline bool QCanDbcFileParserPrivate::parseSignal(const QStringView data)
{
    // The regexp should match the following pattern:
    //      SG_ signal_name multiplexer_indicator : start_bit |
    //      signal_size @ byte_order value_type ( factor , offset )
    //      [ minimum | maximum ] unit receiver {, receiver}
    // We also need to consider the fact that some of the spaces might be
    // optional, and we can potentially allow more spaces between parts.
    // Note that the end of the signal description can contain multiple
    // receivers. The regexp is supposed to extract all of them, but we use
    // only the first one for now.

    // %1 - SignalDef
    // %2 - MaybeSpace
    // %3 - DbcIdentifier
    // %4 - OneOrMoreSpace
    // %5 - MuxIndicator
    // %6 - unsignedInt
    // %7 - byteOrder
    // %8 - valueType
    // %9 - double
    // %10 - charStr
    static const QString regExStr =
            "%1%2(?<name>%3)(%4(?<mux>%5))?%2:%2(?<startBit>%6)%2\\|%2(?<sigSize>%6)%2@%2"
            "(?<byteOrder>%7)%2(?<valueType>%8)%4\\(%2(?<factor>%9)%2,%2(?<offset>%9)%2\\)"
            "%4\\[%2(?<min>%9)%2\\|%2(?<max>%9)%2\\]%4\"(?<unit>%10)\""
            "%4(?<receiver>%3)(%2,%2%3)*"_L1.
            arg(kSignalDef, kMaybeSpaceRegExp, kDbcIdentRegExp, kOneOrMoreSpaceRegExp,
                kMuxIndicatorRegExp, kUnsignedIntRegExp, kByteOrderRegExp, kValueTypeRegExp,
                kDoubleRegExp, kCharStrRegExp);
    static const QRegularExpression signalRegExp(regExStr);

    const auto match = signalRegExp.matchView(data);
    if (match.hasMatch()) {
        QCanSignalDescription desc = extractSignal(match);

        if (desc.isValid())
            m_currentMessage.addSignalDescription(desc);
        else
            addWarning(QObject::tr("Failed to parse signal description from string %1").arg(data));

        m_lineOffset = match.capturedEnd(0);
    } else {
        addWarning(QObject::tr("Failed to find signal description in string %1").arg(data));
        m_lineOffset = data.size(); // skip this string
    }
    return true;
}

//  from ../qtserialbus/src/serialbus/qcandbcfileparser.cpp, line 1132, as _ZN24QCanDbcFileParserPrivate10addWarningEO7QString
inline void QCanDbcFileParserPrivate::addWarning(QString &&warning)
{
    m_warnings.emplace_back(warning);
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

//  bool QCanDbcFileParserPrivate::parseFile(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QCanDbcFileParserPrivate9parseFileERK7QString(
    QCanDbcFileParserPrivate *self,
    const QString *fileName) {
  return self->parseFile(*fileName);
}

//  QCanMessageDescription QCanDbcFileParserPrivate::extractMessage(const
//      QRegularExpressionMatch &match)
extern "C" Q_DECL_EXPORT
QCanMessageDescription *ritual_ZN24QCanDbcFileParserPrivate14extractMessageERK23QRegularExpressionMatch(
    QCanDbcFileParserPrivate *self,
    const QRegularExpressionMatch *match) {
  return new QCanMessageDescription(self->extractMessage(*match));
}

//  bool QCanDbcFileParserPrivate::parseSignal(const QStringView data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QCanDbcFileParserPrivate11parseSignalE11QStringView(
    QCanDbcFileParserPrivate *self,
    const QString *data) {
  return self->parseSignal(QStringView(*data));
}

//  void QCanDbcFileParserPrivate::addWarning(QString &&warning)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCanDbcFileParserPrivate10addWarningEO7QString(
    QCanDbcFileParserPrivate *self,
    QString *warning) {
  self->addWarning(std::move(*warning));
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
