//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/6.12.0/QtNfc/private/qnfctagtype4ndeffsm_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: completed by hand: getCommand and getMessage, with
//  the inline copy of Qt's code they need (QCommandApdu::build). Kept as it
//  is when the generator runs again.
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#include <QtNfc/QtNfc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNfc/6.12.0/QtNfc/private/qnfctagtype4ndeffsm_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtNfc/qndefmessage.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNfc/6.12.0/QtNfc/private/qapduutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qapduutils_p.h"
#include <QtCore/QtEndian>
#include "qnfctagtype4ndeffsm_p.h"
#include <QtCore/QtEndian>
#include <QtCore/QLoggingCategory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/nfc/qapduutils.cpp, line 25, as _ZN13QResponseApduC1ERK10QByteArray
inline QResponseApdu::QResponseApdu(const QByteArray &response)
{
    const auto view = qToByteArrayViewIgnoringNull(response);
    if (view.size() < 2) {
        m_status = Empty;
        m_data = response;
    } else {
        const auto dataSize = view.size() - 2;
        m_status = qFromBigEndian(qFromUnaligned<uint16_t>(view.data() + dataSize));
        m_data = response.left(dataSize);
    }
}

//  from ../qtconnectivity/src/nfc/ndef/qnfctagtype4ndeffsm.cpp, line 158, as _ZN19QNfcTagType4NdefFsm15provideResponseERK10QByteArray
inline QNdefAccessFsm::Action QNfcTagType4NdefFsm::provideResponse(const QByteArray &response)
{
    QResponseApdu apdu(response);

    switch (m_currentState) {
    case SelectApplicationForProbe:
        return handleSimpleResponse(apdu, SelectCCFile, NdefNotSupported);
    case SelectCCFile:
        return handleSimpleResponse(apdu, ReadCCFile, NdefNotSupported);
    case ReadCCFile:
        return handleReadCCResponse(apdu);

    case SelectApplicationForRead:
        return handleSimpleResponse(apdu, SelectNdefFileForRead, NdefSupportDetected);
    case SelectNdefFileForRead:
        return handleSimpleResponse(apdu, ReadNdefMessageLength, NdefSupportDetected);
    case ReadNdefMessageLength:
        return handleReadFileLengthResponse(apdu);
    case ReadNdefMessage:
        return handleReadFileResponse(apdu);

    case SelectApplicationForWrite:
        return handleSimpleResponse(apdu, SelectNdefFileForWrite, NdefSupportDetected);
    case SelectNdefFileForWrite:
        return handleSimpleResponse(apdu, ClearNdefLength, NdefSupportDetected);
    case ClearNdefLength:
        return handleSimpleResponse(apdu, WriteNdefFile, NdefSupportDetected);
    case WriteNdefFile:
        return handleWriteNdefFileResponse(apdu);
    case WriteNdefLength:
        return handleSimpleResponse(apdu, NdefSupportDetected, NdefSupportDetected, Done);

    default:
        return Unexpected;
    }
}

//  from ../qtconnectivity/src/nfc/ndef/qnfctagtype4ndeffsm.cpp, line 93, as _ZN19QNfcTagType4NdefFsm17detectNdefSupportEv
inline QNdefAccessFsm::Action QNfcTagType4NdefFsm::detectNdefSupport()
{
    switch (m_currentState) {
    case SelectApplicationForProbe:
        m_targetState = NdefSupportDetected;
        return SendCommand;
    case NdefSupportDetected:
        return Done;
    case NdefNotSupported:
        return Failed;
    default:
        return Unexpected;
    }
}

//  from ../qtconnectivity/src/nfc/ndef/qnfctagtype4ndeffsm.cpp, line 108, as _ZN19QNfcTagType4NdefFsm12readMessagesEv
inline QNdefAccessFsm::Action QNfcTagType4NdefFsm::readMessages()
{
    switch (m_currentState) {
    case SelectApplicationForProbe:
        m_targetState = NdefMessageRead;
        return SendCommand;
    case NdefSupportDetected:
        m_currentState = SelectApplicationForRead;
        m_targetState = NdefMessageRead;
        return SendCommand;
    case NdefNotSupported:
        return Failed;
    default:
        return Unexpected;
    }
}

//  from ../qtconnectivity/src/nfc/ndef/qnfctagtype4ndeffsm.cpp, line 125, as _ZN19QNfcTagType4NdefFsm13writeMessagesERK5QListI12QNdefMessageE
inline QNdefAccessFsm::Action QNfcTagType4NdefFsm::writeMessages(const QList<QNdefMessage> &messages)
{
    // Only one message per tag is supported
    if (messages.isEmpty() || messages.size() > 1)
        return Failed;

    auto messageData = messages.first().toByteArray();
    if (messageData.size() > m_maxNdefSize - 2)
        return Failed;

    m_ndefData = messageData;

    m_targetState = NdefMessageWritten;

    switch (m_currentState) {
    case SelectApplicationForProbe:
        return SendCommand;

    case NdefNotSupported:
        return Failed;

    case NdefSupportDetected:
        if (!m_writable)
            return Failed;

        m_currentState = SelectApplicationForWrite;
        return SendCommand;

    default:
        return Unexpected;
    };
}

//  from ../qtconnectivity/src/nfc/ndef/qnfctagtype4ndeffsm.cpp, line 195, as _ZN19QNfcTagType4NdefFsm20handleSimpleResponseERK13QResponseApduNS_5StateES3_N14QNdefAccessFsm6ActionE
inline QNdefAccessFsm::Action QNfcTagType4NdefFsm::handleSimpleResponse(
        const QResponseApdu &response, QNfcTagType4NdefFsm::State okState,
        QNfcTagType4NdefFsm::State failedState, QNdefAccessFsm::Action okAction)
{
    if (!response.isOk()) {
        m_currentState = failedState;
        return Failed;
    }

    m_currentState = okState;
    return okAction;
}

//  from ../qtconnectivity/src/nfc/ndef/qnfctagtype4ndeffsm.cpp, line 315, as _ZN19QNfcTagType4NdefFsm28handleReadFileLengthResponseERK13QResponseApdu
inline QNdefAccessFsm::Action
QNfcTagType4NdefFsm::handleReadFileLengthResponse(const QResponseApdu &response)
{
    if (!response.isOk() || response.data().size() < 2) {
        m_currentState = NdefSupportDetected;
        return Failed;
    }

    m_fileSize = qFromBigEndian(qFromUnaligned<uint16_t>(response.data().constData()));
    if (m_fileSize > m_maxNdefSize - 2) {
        m_currentState = NdefSupportDetected;
        return Failed;
    }

    m_fileOffset = 2;
    m_ndefData.clear();

    if (m_fileSize == 0) {
        m_currentState = NdefMessageRead;
        return GetMessage;
    }

    m_currentState = ReadNdefMessage;
    return SendCommand;
}

//  from ../qtconnectivity/src/nfc/ndef/qnfctagtype4ndeffsm.cpp, line 341, as _ZN19QNfcTagType4NdefFsm22handleReadFileResponseERK13QResponseApdu
inline QNdefAccessFsm::Action QNfcTagType4NdefFsm::handleReadFileResponse(const QResponseApdu &response)
{
    if (!response.isOk() || response.data().size() == 0) {
        m_currentState = NdefSupportDetected;
        return Failed;
    }

    auto readSize = qMin<qsizetype>(m_fileSize, response.data().size());
    m_ndefData.append(response.data().first(readSize));
    m_fileOffset += readSize;
    m_fileSize -= readSize;

    if (m_fileSize == 0) {
        m_currentState = NdefMessageRead;
        return GetMessage;
    }

    return SendCommand;
}

//  from ../qtconnectivity/src/nfc/ndef/qnfctagtype4ndeffsm.cpp, line 361, as _ZN19QNfcTagType4NdefFsm27handleWriteNdefFileResponseERK13QResponseApdu
inline QNdefAccessFsm::Action
QNfcTagType4NdefFsm::handleWriteNdefFileResponse(const QResponseApdu &response)
{
    if (!response.isOk()) {
        m_currentState = NdefSupportDetected;
        return Failed;
    }

    if (m_fileSize == 0)
        m_currentState = WriteNdefLength;

    return SendCommand;
}
//  from ../qtconnectivity/src/nfc/qapduutils.cpp, line 41, as _ZN12QCommandApdu5buildEhhhh15QByteArrayViewt
inline QByteArray QCommandApdu::build(uint8_t cla, uint8_t ins, uint8_t p1, uint8_t p2,
                               QByteArrayView data, uint16_t ne)
{
    Q_ASSERT(data.size() <= 0xFFFF);

    QByteArray apdu;
    apdu.append(static_cast<char>(cla));
    apdu.append(static_cast<char>(ins));
    apdu.append(static_cast<char>(p1));
    apdu.append(static_cast<char>(p2));

    bool extendedLc = false;
    uint16_t nc = data.size();

    if (nc > 0) {
        if (nc < 256) {
            apdu.append(static_cast<char>(nc));
        } else {
            extendedLc = true;
            apdu.append('\0');
            apdu.append(static_cast<char>(nc >> 8));
            apdu.append(static_cast<char>(nc & 0xFF));
        }
        apdu.append(data);
    }

    if (ne) {
        if (ne < 256) {
            apdu.append(static_cast<char>(ne));
        } else if (ne == 256) {
            apdu.append(static_cast<char>('\0'));
        } else {
            if (!extendedLc)
                apdu.append('\0');
            apdu.append(static_cast<char>(ne >> 8));
            apdu.append(static_cast<char>(ne & 0xFF));
        }
    }

    return apdu;
}

//  from ../qtconnectivity/src/nfc/ndef/qnfctagtype4ndeffsm.cpp, line 19, as _ZN19QNfcTagType4NdefFsm10getCommandERN14QNdefAccessFsm6ActionE
inline QByteArray QNfcTagType4NdefFsm::getCommand(QNdefAccessFsm::Action &nextAction)
{
    // ID of the NDEF Tag Application
    static constexpr uint8_t NtagApplicationIdV2[] { 0xD2, 0x76, 0x00, 0x00, 0x85, 0x01, 0x01 };
    // Capability container file ID.
    static constexpr uint8_t CapabilityContainerId[] { 0xE1, 0x03 };
    // Shortcut for specifying zero length of NDEF message data.
    static constexpr uint8_t ZeroLength[] { 0x00, 0x00 };

    nextAction = ProvideResponse;

    switch (m_currentState) {
    case SelectApplicationForProbe:
    case SelectApplicationForRead:
    case SelectApplicationForWrite:
        return QCommandApdu::build(0x00, QCommandApdu::Select, 0x04, 0x00,
                                   QByteArrayView::fromArray(NtagApplicationIdV2), 256);
    case SelectCCFile:
        return QCommandApdu::build(0x00, QCommandApdu::Select, 0x00, 0x0C,
                                   QByteArrayView::fromArray(CapabilityContainerId));
    case ReadCCFile:
        return QCommandApdu::build(0x00, QCommandApdu::ReadBinary, 0x00, 0x00, {}, 15);
    case SelectNdefFileForRead:
    case SelectNdefFileForWrite:
        return QCommandApdu::build(0x00, QCommandApdu::Select, 0x00, 0x0C, m_ndefFileId);
    case ReadNdefMessageLength:
        return QCommandApdu::build(0x00, QCommandApdu::ReadBinary, 0x00, 0x00, {}, 2);
    case ReadNdefMessage: {
        uint16_t readSize = qMin(m_fileSize, m_maxReadSize);

        return QCommandApdu::build(0x00, QCommandApdu::ReadBinary, m_fileOffset >> 8,
                                   m_fileOffset & 0xFF, {}, readSize);
    }
    case ClearNdefLength:
        m_fileOffset = 2;
        m_fileSize = m_ndefData.size();
        return QCommandApdu::build(0x00, QCommandApdu::UpdateBinary, 0x00, 0x00,
                                   QByteArrayView::fromArray(ZeroLength));
    case WriteNdefFile: {
        uint16_t updateSize = qMin(m_fileSize, m_maxUpdateSize);
        uint16_t fileOffset = m_fileOffset;

        m_fileOffset += updateSize;
        m_fileSize -= updateSize;

        return QCommandApdu::build(0x00, QCommandApdu::UpdateBinary, fileOffset >> 8,
                                   fileOffset & 0xFF, m_ndefData.mid(fileOffset - 2, updateSize));
    }
    case WriteNdefLength: {
        QByteArray data(2, Qt::Uninitialized);
        qToUnaligned(qToBigEndian<uint16_t>(m_ndefData.size()), data.data());

        return QCommandApdu::build(0x00, QCommandApdu::UpdateBinary, 0x00, 0x00, data);
    }
    default:
        nextAction = Unexpected;
        return {};
    }
}

//  from ../qtconnectivity/src/nfc/ndef/qnfctagtype4ndeffsm.cpp, line 79, as _ZN19QNfcTagType4NdefFsm10getMessageERN14QNdefAccessFsm6ActionE
inline QNdefMessage QNfcTagType4NdefFsm::getMessage(QNdefAccessFsm::Action &nextAction)
{
    if (m_currentState == NdefMessageRead) {
        auto message = QNdefMessage::fromByteArray(m_ndefData);
        m_ndefData.clear();
        m_currentState = NdefSupportDetected;
        nextAction = Done;
        return message;
    }

    nextAction = Unexpected;
    return {};
}

//  -----------------------------------------------------------------------

//  Action QNfcTagType4NdefFsm::provideResponse(const QByteArray &response)
extern "C" Q_DECL_EXPORT
QNdefAccessFsm::Action ritual_ZN19QNfcTagType4NdefFsm15provideResponseERK10QByteArray(
    QNfcTagType4NdefFsm *self,
    const QByteArray *response) {
  return self->provideResponse(*response);
}

//  Action QNfcTagType4NdefFsm::detectNdefSupport()
extern "C" Q_DECL_EXPORT
QNdefAccessFsm::Action ritual_ZN19QNfcTagType4NdefFsm17detectNdefSupportEv(
    QNfcTagType4NdefFsm *self) {
  return self->detectNdefSupport();
}

//  Action QNfcTagType4NdefFsm::readMessages()
extern "C" Q_DECL_EXPORT
QNdefAccessFsm::Action ritual_ZN19QNfcTagType4NdefFsm12readMessagesEv(
    QNfcTagType4NdefFsm *self) {
  return self->readMessages();
}

//  Action QNfcTagType4NdefFsm::writeMessages(const QList<QNdefMessage>
//      &messages)
extern "C" Q_DECL_EXPORT
QNdefAccessFsm::Action ritual_ZN19QNfcTagType4NdefFsm13writeMessagesERK5QListI12QNdefMessageE(
    QNfcTagType4NdefFsm *self,
    const QList<QNdefMessage> *messages) {
  return self->writeMessages(*messages);
}

//  Action QNfcTagType4NdefFsm::handleSimpleResponse(const QResponseApdu
//      &response, State okState, State failedState, Action okAction)
extern "C" Q_DECL_EXPORT
QNdefAccessFsm::Action ritual_ZN19QNfcTagType4NdefFsm20handleSimpleResponseERK13QResponseApduNS_5StateES3_N14QNdefAccessFsm6ActionE(
    QNfcTagType4NdefFsm *self,
    const QResponseApdu *response,
    QNfcTagType4NdefFsm::State okState,
    QNfcTagType4NdefFsm::State failedState,
    QNdefAccessFsm::Action okAction) {
  return self->handleSimpleResponse(
      *response,
      okState,
      failedState,
      okAction);
}

//  Action QNfcTagType4NdefFsm::handleReadFileLengthResponse(const
//      QResponseApdu &response)
extern "C" Q_DECL_EXPORT
QNdefAccessFsm::Action ritual_ZN19QNfcTagType4NdefFsm28handleReadFileLengthResponseERK13QResponseApdu(
    QNfcTagType4NdefFsm *self,
    const QResponseApdu *response) {
  return self->handleReadFileLengthResponse(*response);
}

//  Action QNfcTagType4NdefFsm::handleReadFileResponse(const QResponseApdu
//      &response)
extern "C" Q_DECL_EXPORT
QNdefAccessFsm::Action ritual_ZN19QNfcTagType4NdefFsm22handleReadFileResponseERK13QResponseApdu(
    QNfcTagType4NdefFsm *self,
    const QResponseApdu *response) {
  return self->handleReadFileResponse(*response);
}

//  Action QNfcTagType4NdefFsm::handleWriteNdefFileResponse(const
//      QResponseApdu &response)
extern "C" Q_DECL_EXPORT
QNdefAccessFsm::Action ritual_ZN19QNfcTagType4NdefFsm27handleWriteNdefFileResponseERK13QResponseApdu(
    QNfcTagType4NdefFsm *self,
    const QResponseApdu *response) {
  return self->handleWriteNdefFileResponse(*response);
}

//  Action QNfcTagType4NdefFsm::detectNdefSupport()
extern "C" Q_DECL_EXPORT
QNdefAccessFsm::Action ritual_own_ZN19QNfcTagType4NdefFsm17detectNdefSupportEv(
    QNfcTagType4NdefFsm *self) {
  return self->QNfcTagType4NdefFsm::detectNdefSupport();
}

//  Action QNfcTagType4NdefFsm::readMessages()
extern "C" Q_DECL_EXPORT
QNdefAccessFsm::Action ritual_own_ZN19QNfcTagType4NdefFsm12readMessagesEv(
    QNfcTagType4NdefFsm *self) {
  return self->QNfcTagType4NdefFsm::readMessages();
}

//  QByteArray QNfcTagType4NdefFsm::getCommand(Action &nextAction)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN19QNfcTagType4NdefFsm10getCommandERN14QNdefAccessFsm6ActionE(
    QNfcTagType4NdefFsm *self,
    QNdefAccessFsm::Action *nextAction) {
  return new QByteArray(self->getCommand(*nextAction));
}

//  QNdefMessage QNfcTagType4NdefFsm::getMessage(Action &nextAction)
extern "C" Q_DECL_EXPORT
QNdefMessage *ritual_ZN19QNfcTagType4NdefFsm10getMessageERN14QNdefAccessFsm6ActionE(
    QNfcTagType4NdefFsm *self,
    QNdefAccessFsm::Action *nextAction) {
  return new QNdefMessage(self->getMessage(*nextAction));
}
